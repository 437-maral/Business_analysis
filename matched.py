import pandas as pd 


def matched_extraction(ground_truth, extracted_data, name_field):
    extraction = extracted_data.copy()
    name_column_match = f"match_extraction_{name_field}"
    extraction[name_column_match] = None

    for document in extraction["document_id"].unique():
        # Filter rows based on document_id
        matching_rows_ex = extraction[extraction["document_id"] == document]
        matching_rows_gt = ground_truth[ground_truth["document_id"] == document]

        for i, row_ex in matching_rows_ex.iterrows():
            each_line_to_compare_ex = row_ex[f"{name_field}_original"]
            position_ex = row_ex["running_index"]
            
   
            match_duplicated = False
            
            # Iterate over rows in the ground truth data
            for j, row_gt in matching_rows_gt.iterrows():
                each_line_to_compare_gt = row_gt[f"gt_{name_field}"]
                position_gt = row_gt["gt_line_item"]

                # Compare values and assign match status
                if each_line_to_compare_ex == each_line_to_compare_gt:
                    if position_ex == position_gt:
                        match_duplicated = True
                        extraction.loc[i, name_column_match] = "match"
                        break
                    elif position_ex != position_gt:
                        if not match_duplicated:
                            extraction.loc[i, name_column_match] = "position_mismatch"
                            match_duplicated = True
                        #else:
                            #extraction.loc[i, name_column_match] = "exceptional_case"
            
            # If no match was found for this row
            if not match_duplicated:
                extraction.loc[i, name_column_match] = "no_match"

    return extraction




def matched_business_change(ground_truth, extraction, name_field):
    name_column_match = f"match_corrected_{name_field}"
    extraction[name_column_match] = None  # Default value

    for document in extraction["document_id"].unique():
        # Filter rows for the current document
        matching_rows_ex = extraction[extraction["document_id"] == document]
        matching_rows_gt = ground_truth[ground_truth["document_id"] == document]

        for i, row_ex in matching_rows_ex.iterrows():
            position_ex = row_ex["running_index"]
            each_line_to_compare_ex = row_ex.get(f"{name_field}_original", "")
            each_line_to_compare_corr = row_ex.get(f"{name_field}_corrected", "")
            
            match_found = False

            for _, row_gt in matching_rows_gt.iterrows():
                position_gt = row_gt["gt_line_item"]
                each_line_to_compare_gt = row_gt.get(f"gt_{name_field}", "")

                if position_ex == position_gt:
                    if each_line_to_compare_ex == each_line_to_compare_gt:
                        if each_line_to_compare_corr == each_line_to_compare_gt:
                            extraction.loc[i, name_column_match] = "match,no change"
                        else:
                            extraction.loc[i, name_column_match] = "match,pe business"
                        match_found = True
                        break
                else:
                    if each_line_to_compare_ex == each_line_to_compare_gt:
                        if each_line_to_compare_corr == each_line_to_compare_gt:
                            extraction.loc[i, name_column_match] = "position_mismatch,no change"
                        else:
                            extraction.loc[i, name_column_match] = "position_mismatch,pe business"
                        match_found = True

            if not match_found:
                if each_line_to_compare_ex != each_line_to_compare_gt and  each_line_to_compare_corr != each_line_to_compare_gt:
                    extraction.loc[i, name_column_match] = "extraction error,business change"

    return extraction

def determine_filed_check(row,field):
    if row[f"match_extraction_{field}"] in ("match", "position_mismatch") and row[f"match_corrected_{field}"] in ("match,no change", "position_mismatch,no change"):
        return "Perfect Extraction"
    elif row[f"match_corrected_{field}"] in ("match,pe business", "position_mismatch,pe business"):
        return "Perfect Extraction, Business Change"
    elif row[f"match_corrected_{field}"] == "extraction error,business change":
        return "Extraction error,Business change"
    else:
        return "Extraction Error"   