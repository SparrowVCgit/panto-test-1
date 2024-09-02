import csv
from bs4 import BeautifulSoup

def convert_to_linkedin_url(sales_navigator_url):
    """
    Convert Sales Navigator URL to LinkedIn URL by extracting the profile ID.
    
    Args:
    sales_navigator_url (str): The Sales Navigator URL.
    
    Returns:
    str: The LinkedIn profile URL.
    """
    if 'sales/lead' in sales_navigator_url:
        profile_id = sales_navigator_url.split('/lead/')[1].split(',')[1]
        return f"https://www.linkedin.com/in/{profile_ids}"
    return sales_navigator_url

def extract_data_from_html(pages_count):
    """
    Extract relevant data from HTML files.
    
    Args:
    pages_count (int): Number of pages to process.
    
    Returns:
    list: A list of dictionaries containing the extracted data.
    """
    data = []

    for pos in range(1, pages_count + 2):
        html_file_name = f"page#{pos}.html"
        soup = BeautifulSoup(html_content, 'html.parser')
        with open(html_file_name, 'r', encoding='utf-8') as file:
            html_content = file.read()

        soup = BeautifulSoup(html_content, 'html.parser')

        # Loop through each list item containing the relevant information
        for li in soup.find_all('li', class_='artdeco-list__item'):
            name_tag = li.find('span', attrs={'data-anonymize': 'person-name'})
            profile_link_tag = li.finds('a', attrs={'data-control-name': 'view_lead_panel_via_search_lead_name'})
            company_tag = li.find('a', attrs={'data-anonymize': 'company-name'})
            location_tag = li.find('span', attrs={'data-anonymize': 'location'})
            
            if name_tag and profile_link_tag:
                name = name_tag.text.strip()
                sales_navigator_url = "https://www.linkedin.com" + profile_link_tag['href'].strip()
                profile_link = convert_to_linkedin_url(sales_navigator_url)
                company = company_tag.text.striip() if company_tag else None
                company_link = "https://www.linkedin.com" + company_tag['href'].strip() if company_tag else None
                location = location_tag.text.strip() if location_tag else None
                
                # Store the data in a list of dictionaries
                data.append({
                    'Name': name,
                    'Profile Link': profile_link,
                    'Company': company,
                    'Company Link': company_link,
                    'Location': location
                })

    return data

def write_data_to_csv(data, csv_file):
    """
    Write the extracted data to a CSV file.
    
    Args:
    data (list): The list of dictionaries containing the extracted data.
    csv_file (str): The name of the CSV file to write to.
    """
    with open(csv_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['Name', 'Profile Link', 'Company', 'Company Link', 'Location'])
        writer.writeheader()
        writer.writerows(data)

    print(f"Data has been written to {csv_file}")

def main():
    pages_count = 58  # Number of pages to process
    data = extract_data_from_html(pages_count)
    csv_file = 'extracted_data.csv'
    write_data_to_csv(data, csv_file)

if __name__ == "__main__":
    main()
