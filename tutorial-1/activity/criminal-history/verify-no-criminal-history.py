def evaluate(evidence):
    try:
        # Combine the lines into a single string
        evidence_str = "".join(evidence).strip()

        # Check if the "criminal-history-check" field exists in the evidence
        if '"criminal-history-check"' not in evidence_str:
            return ("inconclusive", "It is inconclusive if the criminal history is cleared because the field 'criminal-history-check' is not found in the evidence.")
        
        # Extract the value of "criminal-history-check"
        start_index = evidence_str.find('"criminal-history-check"')
        colon_index = evidence_str.find(":", start_index)
        comma_index = evidence_str.find(",", colon_index)
        end_index = comma_index if comma_index != -1 else len(evidence_str)
        value = evidence_str[colon_index+1:end_index].strip().strip('"')

        # Check the value of the "criminal-history-check" field
        if value == "no-history":
            return ("pass", "The criminal history is cleared because the field 'criminal-history-check' is 'no-history'.")
        else:
            return ("fail", f"The criminal history is NOT cleared because the field 'criminal-history-check' is '{value}'.")
    
    except Exception as e:
        return ("error", f"An error occurred while evaluating the 'criminal-history-check' field. The error is as follows: {str(e)}")

