# features/response_manager.py
responses = {
    "who_are_you": {
        "english": "I am Rob, a multilingual AI created by Ibrahim.",
        "roman": "Main Rob hoon, ek AI jo Ibrahim ne banaya hai.",
        "urdu": "میں روب ہوں، ایک ذہین چیٹ بوٹ جو ابراہیم نے بنایا۔"
    },
    "how_are_you": {
        "english": "I'm doing great! How about you?",
        "roman": "Main theek hoon! Tum kaisay ho?",
        "urdu": "میں ٹھیک ہوں! آپ کیسے ہیں؟"
    },
    "your_hobbies": {
        "english": "I enjoy learning, chatting with humans, and improving myself.",
        "roman": "Mujhe seekhna, logon se baat karna aur apne aap ko behtar banana pasand hai.",
        "urdu": "مجھے سیکھنا، انسانوں سے بات کرنا اور خود کو بہتر بنانا پسند ہے۔"
    },
    "joke": {
        "english": "Why did the computer go to school? Because it had a lot to learn!",
        "roman": "Computer school kyu gaya? Kyun ke usay bohat kuch seekhna tha!",
        "urdu": "کمپیوٹر اسکول کیوں گیا؟ کیونکہ اسے بہت کچھ سیکھنا تھا!"
    }
}

def get_response(key, lang):
    return responses.get(key, {}).get(lang, "I'm still learning! Try asking something else.")
