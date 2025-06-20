# cli.py
import sys
import csv
from dotenv import load_dotenv
load_dotenv()

from validator import validate_row
from geo import enhance_with_geo

def main():
    if '--help' in sys.argv or len(sys.argv) < 2:
        print("Usage: cli.py <input.csv> [output.csv]")
        return

    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None

    try:
        with open(input_file, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            output = open(output_file, 'w', newline='', encoding='utf-8') if output_file else sys.stdout
            writer = csv.writer(output)

            header = next(reader, None)
            if header:
                header += ['res_lat', 'res_lng', 'post_lat', 'post_lng']
                writer.writerow(header)

            for i, row in enumerate(reader, 2):
                if len(row) < 16:
                    print(f"Line {i}: Skipping invalid row (not enough fields): {row}", file=sys.stderr)
                    continue

                if not validate_row(row):
                    print(f"Line {i}: Validation failed: {row}", file=sys.stderr)
                    continue

                enriched_row = enhance_with_geo(row.copy())
                if enriched_row:
                    writer.writerow(enriched_row)
                else:
                    print(f"Line {i}: Geolocation failed for: {row}", file=sys.stderr)

            if output_file:
                output.close()

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == '__main__':
    main()
