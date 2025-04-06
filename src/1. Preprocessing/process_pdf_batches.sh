#!/bin/bash

# Script to process a PDF in batches using marker_single, separating output and logs (ATTEMPT 9)

# --- Configuration ---
PDF_FILE="$1"            # Path to the PDF file
BATCH_SIZE="${2:-10}"    # Pages per batch (default: 10)
OUTPUT_DIR="${3:-output}"  # Output directory (MUST EXIST)
USE_OLLAMA="${4:-false}"  # Use Ollama (default: false)
OLLAMA_MODEL="${5:-deepseek-r1:8b}"  # Ollama model name (default: "deepseek-r1:8b")
LOG_FILE="$OUTPUT_DIR/process_log.txt" # Log file
# --- End Configuration ---

# --- Helper Functions ---
error() {
  echo "$(date) ERROR: $1" | tee -a "$LOG_FILE" >&2
  exit 1
}

log() {
  echo "$(date) INFO: $1" | tee -a "$LOG_FILE"
}

get_page_count() {
  if ! command -v pdfinfo &> /dev/null; then
    error "pdfinfo not installed (poppler-utils)."
  fi
  pdfinfo "$PDF_FILE" | grep '^Pages:' | awk '{print $2}'
}
# --- End Helper Functions ---

# --- Validation ---
if [ -z "$PDF_FILE" ]; then error "PDF file required."; fi
if [ ! -f "$PDF_FILE" ]; then error "PDF file not found."; fi
if ! [[ "$BATCH_SIZE" =~ ^[0-9]+$ ]]; then error "Invalid batch size."; fi
if [ ! -d "$OUTPUT_DIR" ]; then error "Output directory missing."; fi
if [ ! -f "$LOG_FILE" ]; then touch "$LOG_FILE"; fi
if ! command -v marker_single &> /dev/null; then error "marker_single not found in PATH."; fi
if [ "$USE_OLLAMA" != "true" ] && [ "$USE_OLLAMA" != "false" ]; then
  error "Invalid value for USE_OLLAMA. Must be 'true' or 'false'."
fi

# Clean existing output files
if [ -f "$LOG_FILE" ]; then
  > "$LOG_FILE"
  log "Cleared existing log file: $LOG_FILE"
fi
if [ -f "$FINAL_MARKDOWN" ]; then
  > "$FINAL_MARKDOWN"
  log "Cleared existing output file: $FINAL_MARKDOWN"
fi
# --- End Validation ---

# Extract base filename (without .pdf)
BASE_NAME=$(basename "$PDF_FILE" .pdf)
FINAL_MARKDOWN="$OUTPUT_DIR/$BASE_NAME.md"

# Clear final output file if exists
: > "$FINAL_MARKDOWN"

# --- Main Script ---
TOTAL_PAGES=$(get_page_count)
log "Total pages: $TOTAL_PAGES"

START_PAGE=0
while [ "$START_PAGE" -lt "$TOTAL_PAGES" ]; do
  END_PAGE=$((START_PAGE + BATCH_SIZE - 1))
  if [ "$END_PAGE" -ge "$TOTAL_PAGES" ]; then
    END_PAGE=$((TOTAL_PAGES - 1))
  fi

  log "Processing pages $START_PAGE-$END_PAGE"
  PAGE_RANGE="$START_PAGE-$END_PAGE"

  # Temp output path from marker_single
  TEMP_DIR="$OUTPUT_DIR/$BASE_NAME"
  TEMP_MD="$TEMP_DIR/${BASE_NAME}.md"

  # Execute marker_single
  LLM_OPTIONS=""
  if [[ "$USE_OLLAMA" = "true" ]]; then
    # Verify if LLM-related options are supported
    if echo "--use_llm" | grep -q -- "--use_llm"; then
      LLM_OPTIONS="--use_llm --TableConverter_use_llm --llm_service marker.services.ollama.OllamaService --ollama_model \"$OLLAMA_MODEL\""
    else
      error "LLM-related options are not supported by the installed version of marker_single."
    fi
  fi

  CMD="marker_single \
      --disable_ocr \
      --disable_image_extraction \
      --output_format markdown \
      --output_dir \"$OUTPUT_DIR\" \
      --page_range \"$PAGE_RANGE\" \
      $LLM_OPTIONS \
      \"$PDF_FILE\""

  log "Executing command: $CMD"

  if eval "$CMD" >> "$LOG_FILE" 2>&1; then
    if [ -f "$TEMP_MD" ]; then
      cat "$TEMP_MD" >> "$FINAL_MARKDOWN"
      log "Appended pages $START_PAGE-$END_PAGE to $FINAL_MARKDOWN"
      rm -rf "$TEMP_DIR"
    else
      error "Markdown file not found: $TEMP_MD"
    fi

  else
    error "Error processing pages $START_PAGE-$END_PAGE. Check log for details."
  fi

  START_PAGE=$((END_PAGE + 1))
done

log "Processing complete. Output saved to $FINAL_MARKDOWN"
exit 0
