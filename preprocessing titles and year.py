import pandas as pd
import re

def rearrange_title(title):
    # Regex to identify titles with multiple parentheses and reorder them
    complex_pattern = re.compile(r'^(.*),\s*(The|A|An|Les)\s*\(([^)]+)\)\s*\((\d{4})\)$')
    simple_pattern = re.compile(r'^(.*),\s*(The|A|An|Les)\s*(\(\d{4}\))$')

    complex_match = complex_pattern.match(title)
    simple_match = simple_pattern.match(title)

    if complex_match:
        base_title = complex_match.group(1)
        prefix = complex_match.group(2)
        year = complex_match.group(4)
        return f"{prefix} {base_title} ({year})"
    elif simple_match:
        base_title = simple_match.group(1)
        prefix = simple_match.group(2)
        year = simple_match.group(3)
        return f"{prefix} {base_title} {year}"
    else:
        return title

def extract_year_and_clean_title(title):
    # Regular expression to find the year and any additional details in the title
    year_pattern = re.compile(r'\((\d{4})\)$')
    extra_details_pattern = re.compile(r'\s*\([^)]+\)\s*')

    # Extract the year
    year_match = year_pattern.search(title)
    if year_match:
        year = year_match.group(1)
        # Remove the year from the title
        title = year_pattern.sub('', title)
    else:
        year = None

    # Remove any additional details from the title
    title = extra_details_pattern.sub('', title).strip()

    return title, year

def preprocess_movie_dataset(file_path, output_path):
    # Load the dataset
    movies_df = pd.read_csv(file_path)

    # Apply the function to rearrange titles first
    movies_df['title'] = movies_df['title'].apply(rearrange_title)

    # Apply the function to extract year and clean the title
    new_data = movies_df['title'].apply(lambda x: pd.Series(extract_year_and_clean_title(x), index=['title', 'year']))

    # Assign the cleaned titles and year to the dataframe
    movies_df['title'] = new_data['title']
    movies_df['year'] = new_data['year']

    # Save the preprocessed dataset
    movies_df.to_csv(output_path, index=False)
    print("Dataset saved to", output_path)

# Set the path to your original dataset
input_file_path = '/Users/Mathi/Desktop/movies.csv'
output_file_path = '/Users/Mathi/Desktop/preprocessed_movie_dataset2.csv'

# Run the preprocessing function
preprocess_movie_dataset(input_file_path, output_file_path)
