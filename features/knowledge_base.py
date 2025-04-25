import langid

def get_smart_response(user_input):
    # Detect language using langid
    lang, _ = langid.classify(user_input)

    # Check for English, Urdu, or Roman Urdu
    if lang == 'en':
        # Handle specific English questions like "How are you?"
        if "how are you" in user_input.lower():
            return "I'm doing great, thank you for asking!"
    
    elif lang == 'ur':
        # Handle specific Urdu questions like "Kese ho?"
        if "kese ho" in user_input.lower() or "aap kaise hain" in user_input.lower():
            return "Main bilkul theek hoon, shukriya aap kaise hain?"
    
    # If it looks like Roman Urdu (a mix of English and Urdu), handle it
    elif any(word in user_input.lower() for word in ["kese", "hai", "ho", "tum", "aap", "kaise", "kya", "hoon", "thume"]):
        return "Mujay ibrahim ne bade mushkil se banaya hai"
    
    else:
        return "I couldn't detect the language properly, but I'm learning more every day!"
    
