import os
import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class PDFPrintHandler(FileSystemEventHandler):
    def __init__(self, printer_name, delay=10):
        self.printer_name = printer_name
        self.delay = delay  # Delay in seconds before printing
        self.processed_files = set()  # Keep track of processed files

    def on_created(self, event):
        if event.is_directory:
            return
        if event.src_path.endswith(".pdf"):
            # Check if the file has already been processed
            if event.src_path in self.processed_files:
                print(f"File {event.src_path} has already been processed. Skipping...")
                return

            print(f"Detected new file: {event.src_path}")
            time.sleep(self.delay)  # Wait for the specified delay
            self.print_pdf(event.src_path)
            self.delete_pdf(event.src_path)
            # Add the file to the processed set
            self.processed_files.add(event.src_path)

    def print_pdf(self, pdf_path):
        # Use SumatraPDF to print the PDF
        try:
            # Path to SumatraPDF executable
            sumatra_path = r"PATH"
            # Command to print PDF using SumatraPDF
            command = [
                'cmd.exe', '/C', sumatra_path, '-print-to', self.printer_name, pdf_path
            ]
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            process.communicate()  # Wait for the command to finish
            print(f"Sent {pdf_path} to printer: {self.printer_name}")
        except Exception as e:
            print(f"Error printing {pdf_path}: {e}")

    def delete_pdf(self, pdf_path):
        try:
            os.remove(pdf_path)
            # Wait a moment to ensure the file is deleted
            time.sleep(0.5)
            if not os.path.exists(pdf_path):
                print(f"Deleted: {pdf_path}")
            else:
                print(f"Failed to delete: {pdf_path}")
        except Exception as e:
            print(f"Error deleting {pdf_path}: {e}")

def monitor_folder(folder_path, printer_name, delay):
    event_handler = PDFPrintHandler(printer_name, delay)
    observer = Observer()
    observer.schedule(event_handler, folder_path, recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    folder_to_monitor = r"PATH"
    printer_name = "PRINTER"
    delay_before_printing = 1  # Adjust this delay as needed (in seconds)
    monitor_folder(folder_to_monitor, printer_name, delay_before_printing)
