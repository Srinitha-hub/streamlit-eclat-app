import streamlit as st
import json

def main():
    st.title('Eclat Input')

    # Textarea for user input
    input_items = st.text_area('Enter transactions separated by new lines and items separated by commas (,):')

    # Number input for minimum support threshold
    min_support = st.number_input('Minimum Support Threshold:', min_value=1, value=2)

    # Calculate frequent itemsets on button click
    if st.button('Calculate'):
        frequent_itemsets, support_count = calculate_eclat(input_items, min_support)
        
        # Display frequent itemsets and their support
        if frequent_itemsets:
            formatted_output = {item: count for item, count in support_count.items() if count >= min_support}
            st.json(formatted_output)
        else:
            st.write('No frequent itemsets found.')

def calculate_eclat(input_items, min_support):
    transactions = [line.strip().split(',') for line in input_items.split('\n') if line.strip()]
    
    # Calculate support for each item
    support_count = {}
    for transaction in transactions:
        for item in transaction:
            if item:
                support_count[item] = support_count.get(item, 0) + 1
    
    return [item for item, count in support_count.items() if count >= min_support], support_count

if __name__ == '__main__':
    main()
