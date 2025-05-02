from transformers import pipeline
from convert_to_json import convert_to_json

def format_input(title, store, manufacturer):
    """
    Format the input for the model.
    """
    # Ensure all inputs are strings
    title = str(title)
    store = str(store)
    manufacturer = str(manufacturer)

    # Create the input text

    input_text = (
            f"Classify product:\n"
            f"Title: {title}\n"
            f"Store: {store}\n"
            f"Manufacturer: {manufacturer}"
        )
    
    return input_text

def predict(pipe, title, store, manufacturer):
    """
    Predict the category of the product using the model pipeline.
    """
    # Format the input
    input_text = format_input(title, store, manufacturer)

    # Make prediction
    prediction = pipe(input_text, max_length=384, clean_up_tokenization_spaces=True)

    # structured json data
    print(convert_to_json(prediction[0]['generated_text']))

    return prediction[0]['generated_text']

def main():
    # Load the model pipeline
    pipe = pipeline(
        "text2text-generation",
        model="SurAyush/title2metadata"
    )

    # training set example
    # title = "Hellwig 7860 UTV Powersports Rear Sway Bar for Polaris Ranger 800"
    # store = "Hellwig"
    # manufacturer = "Hellwig"

    # expected out 
    # "details_Brand": "Hellwig", "L0_category": "Automotive", "L1_category": "Replacement Parts", "L2_category": "Shocks, Struts & Suspension", "L3_category": "Sway Bars & Parts", "L4_category": "Sway Bars"}

    # validation example
    # title = "Lenox Organics Ruffle Crystal Vase, Smoke"
    # store = "Lenox"
    # manufacturer = "Lenox"

    # expected out
    # "details_Brand": "Lenox", "L0_category": "Home & Kitchen", "L1_category": "Home Dcor Products", "L2_category": "Vases", "L3_category": "na", "L4_category": "na"}

    # random example from amazon
    title = "Homefab India 2 Piece Velvet Window Curtains - 5 feet, Brown"
    store = "Homefab"
    manufacturer = "Homefab India"

    # Get prediction
    prediction = predict(pipe, title, store, manufacturer)
    print(prediction)

if __name__ == "__main__":
    main()