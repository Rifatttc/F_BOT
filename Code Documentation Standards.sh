def download_public_media(url: str, temp_dir: str) -> dict:
    """
    Downloads private media from provided URL.
    
    Args:
        url (str): Valid URL to private content
        temp_dir (str): Path to temporary storage directory
    
    Returns:
        dict: {
            'success': bool,
            'files': list of file paths,
            'media_type': str ('photo'|'video'|'document'),
            'error': str (if success=False)
        }
    
    Raises:
        ValueError: If URL format is invalid
        PermissionError: If content is not publicly accessible
    """
