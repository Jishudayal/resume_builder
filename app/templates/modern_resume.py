def modern_resume(data):
    return f"""
    <div style="font-family: 'Roboto', sans-serif; color: #333;">
        <h1>{data['Name']}</h1>
        <h2>{data['Email']}</h2>
        <p>{data['Summary']}</p>
    </div>
    """
