def build_prompt(dataset_description, rows, output_format):
    """Build the prompt used to generate a synthetic dataset."""

    return f"""
Generate a realistic synthetic dataset based on the following description.

Dataset Description:
{dataset_description}

Requirements:
- Generate exactly {rows} rows.
- Output format: {output_format}.
- Include column headers.
- Make the data realistic and internally consistent.
- Do not repeat identical rows.
- Return only the dataset.
- Do not include explanations, markdown, code fences, or additional text.
- Ensure realistic values.
- Ensure numerical consistency.
- Ensure every row is unique.
"""