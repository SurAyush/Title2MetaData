import json
import re

def convert_to_json(text):
    try:
        # find keys that are not enclosed in quotes and enclose them in double quotes
        text = re.sub(r'(\s*)(\w+):', r'\1"\2":', text)

        # Enclose the string in curly braces if not already
        if not text.strip().startswith('{'):
            text = '{' + text
        if not text.strip().endswith('}'):
            text = text + '}'

        # Replace single quotes with double quotes
        text = text.replace("'", '"')

        # Convert to JSON
        data = json.loads(text)

        # Optional: Define required fields
        required_fields = [
            "details_Brand", "L0_category", "L1_category",
            "L2_category", "L3_category", "L4_category"
        ]

        # Check for missing fields
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            raise ValueError(f"Missing required fields: {missing_fields}, model_output: {text}")

        return data

    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON format: {e}")
    except Exception as e:
        raise ValueError(f"Error converting to JSON: {e}")
