def detect_disease(user_text):
    if "पीले पत्ते" in user_text or "yellow leaves" in user_text:
        return "यह Nutrient Deficiency हो सकती है। Organic Treatment: Neem Oil Spray।"
    elif "काला धब्बा" in user_text or "black spots" in user_text:
        return "यह Fungal Infection हो सकता है। Treatment: Copper Fungicide Spray।"
    else:
        return "मुझे समस्या समझ नहीं आई, कृपया और जानकारी दें।"
