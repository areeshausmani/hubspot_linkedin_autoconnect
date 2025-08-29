import re

def clean_linkedin_url(url: str) -> str:
    """
    Normalize and validate LinkedIn URLs.
    Removes tracking params and enforces correct format.
    """
    if not url:
        return ""
    # Strip whitespace
    url = url.strip()
    # Remove URL parameters
    url = url.split("?")[0]
    # Ensure it starts with https://
    if not url.startswith("https://"):
        url = "https://" + url
    # Basic validation
    if not re.match(r"https:\/\/(www\.)?linkedin\.com\/.*", url):
        return ""
    return url

if __name__ == "__main__":
    # Demo
    sample_url = "www.linkedin.com/in/jane-doe-123?trk=contacts"
    print("Original:", sample_url)
    print("Cleaned :", clean_linkedin_url(sample_url))
