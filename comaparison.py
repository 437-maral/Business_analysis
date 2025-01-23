
import pandas as pd

def check_po_number(ground_truth, extracted_data, name_field):
    extraction=extracted_data.copy()
    
    for document in extraction["document_id"].unique():
        # Filter rows based on document_id
        matching_rows_ex = extraction[extraction["document_id"] == document]
        matching_rows_gt = ground_truth[ground_truth["document_id"] == document]
        # Iterate over rows in the extracted data
        for i, row_ex in matching_rows_ex.iterrows():
            each_po_to_compare_ex = row_ex[f"{name_field}_original"]
            each_po_to_compare_corr = row_ex[f"{name_field}_corrected"]
            
            for j, row_gt in matching_rows_gt.iterrows():
                each_po_to_compare_gt = row_gt[f"gt_{name_field}"]


        if each_po_to_compare_ex  == each_po_to_compare_gt:
            extraction.at[i, "PO_Number_Check"] = "Perfect Extraction"
         
        # Extraction Error 
        if each_po_to_compare_ex  != each_po_to_compare_gt:
            if each_po_to_compare_gt == each_po_to_compare_corr:
                extraction.at[i, "PO_Number_Check"] = "Extraction Error"
            elif each_po_to_compare_corr != each_po_to_compare_gt:
                extraction.at[i, "PO_Number_Check"] = "Business change+Extraction Error"

     
        #Business Change  
        if each_po_to_compare_ex == each_po_to_compare_gt and each_po_to_compare_corr != each_po_to_compare_gt:
            extraction.at[i, "PO_Number_Check"] = "Perfect Extraction,Business Change"

        

    return extraction



def check_po_date(ground_truth, extracted_data, name_field):
    extraction=extracted_data.copy()
    
    for document in extraction["document_id"].unique():
        # Filter rows based on document_id
        matching_rows_ex = extraction[extraction["document_id"] == document]
        matching_rows_gt = ground_truth[ground_truth["document_id"] == document]
        # Iterate over rows in the extracted data
        for i, row_ex in matching_rows_ex.iterrows():
            each_po_to_compare_ex = row_ex[f"{name_field}_original"]
            each_po_to_compare_corr = row_ex[f"{name_field}_corrected"]
            
            for j, row_gt in matching_rows_gt.iterrows():
                each_po_to_compare_gt = row_gt[f"gt_{name_field}"]


        if each_po_to_compare_ex  == each_po_to_compare_gt:
            extraction.at[i, "PO_Date_Check"] = "Perfect Extraction"
         
        # Extraction Error 
        if each_po_to_compare_ex  != each_po_to_compare_gt:
            if each_po_to_compare_gt == each_po_to_compare_corr:
                extraction.at[i, "PO_Date_Check"] = "Extraction Error"
            elif each_po_to_compare_corr != each_po_to_compare_gt:
                extraction.at[i, "PO_Date_Check"] = "Business change+Extraction Error"

     
        #Business Change  
        if each_po_to_compare_ex == each_po_to_compare_gt and each_po_to_compare_corr != each_po_to_compare_gt:
            extraction.at[i, "PO_Date_Check"] = "Perfect Extraction,Business Change"

        

    return extraction






def check_doctype(ground_truth, extraction, name_field):
    for document in extraction["document_id"].unique():
        # Filter rows based on document_id
        matching_rows_ex = extraction[extraction["document_id"] == document]
        matching_rows_gt = ground_truth[ground_truth["document_id"] == document]
        # Iterate over rows in the extracted data
        for i, row_ex in matching_rows_ex.iterrows():
            each_po_to_compare_ex = row_ex[f"{name_field}_original"]
            each_po_to_compare_corr = row_ex[f"{name_field}_corrected"]
            
            for j, row_gt in matching_rows_gt.iterrows():
                each_po_to_compare_gt = row_gt[f"gt_{name_field}"]


        if each_po_to_compare_ex  == each_po_to_compare_gt:
            extraction.at[i, "DOCType_Check"] = "Perfect Extraction"
         
        # Extraction Error 
        if each_po_to_compare_ex  != each_po_to_compare_gt:
            if each_po_to_compare_gt == each_po_to_compare_corr:
                extraction.at[i, "DOCType_Check"] = "Extraction Error"
            elif each_po_to_compare_corr != each_po_to_compare_gt:
                extraction.at[i, "DOCType_Check"] = "Business change+Extraction Error"

     
        #Business Change  
        if each_po_to_compare_ex == each_po_to_compare_gt and each_po_to_compare_corr != each_po_to_compare_gt:
            extraction.at[i, "DOCType_Check"] = "Perfect Extraction,Business Change"

        

    return extraction























































