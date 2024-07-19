import streamlit as st
import json
from T02_task2 import analyze_reviews, draft_emails, reviews

def main():
    st.title("Review Analyzer and Email Generator")
    st.header("Email Drafts Based on Customer Reviews")
    analyzed_reviews = analyze_reviews(reviews)
    email_prompts = draft_emails(analyzed_reviews)
    with open("reviews.json", "w") as f:
        data_to_save = [dict(review, email_content=email_prompts[i]) for i, review in enumerate(analyzed_reviews)]
        json.dump(data_to_save, f, indent=4)
    for review in data_to_save:
        st.subheader(f"Email for {review['customer_name']} ({review['customer_email']})")
        st.write(f"Sentiment: {review['sentiment']}")
        st.write("Drafted Email:")
        st.write(review['email_content'])
        st.write("---")

if __name__ == "__main__":
    main()
