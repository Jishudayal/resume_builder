def classic_resume(data):
    return f"""
    <div style="font-family: 'Georgia', serif; color: #000;">
        <h1>{data['Name']}</h1>
        <h2>{data['Email']}</h2>
        <p>{data['Summary']}</p>
    </div>
    """
