from bs4 import BeautifulSoup

def extract_usernames_from_html(file_path):
    """
    Extracts usernames from an Instagram HTML file.
    Args: 
        file_path (str): The path to the HTML file.
    Returns:
        set: A set of usernames extracted from the HTML file.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        soup = BeautifulSoup(content, 'html.parser')
        links = soup.find_all('a', href=True)
        usernames = {link['href'].split('/')[-1] for link in links if 'instagram.com' in link['href']}
    return usernames

def find_non_followers(followers_file, following_file):
    """
    Compares two lists of Instagram usernames and finds who doesn't follow back.
    Args:
        followers_file (str): Path to the HTML file containing the list of followers.
        following_file (str): Path to the HTML file containing the list of following.
    Returns:
        set: A set of usernames who don't follow back.
    """
    followers = extract_usernames_from_html(followers_file)
    following = extract_usernames_from_html(following_file)
    return following - followers

# Paths to HTML files
followers_file = r'/Users/priyankabajaj/Downloads/instagram-priyaaannkaa-2024-02-13-fNnNVeFY/connections/followers_and_following/followers_1.html'
following_file = r'/Users/priyankabajaj/Downloads/instagram-priyaaannkaa-2024-02-13-fNnNVeFY/connections/followers_and_following/following.html'

# Find non-followers
non_followers = find_non_followers(followers_file, following_file)

# Display the results
if non_followers:
    print("Accounts that don't follow you back:")
    for i, username in enumerate(non_followers, 1):
        print(f"{i}. {username}")
else:
    print("Everyone you follow also follows you back!")