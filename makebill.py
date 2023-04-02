from docxtpl import DocxTemplate
# Bill No.	289/2022-23	Dated:	13-01-2022



sentence_list = [{'Property A:':'Land measuring 0.1990 Hectare, out of 0.328 Hectare (new khasra no. 332), bearing proposed Gata number 157/3, 160 and 170 of Chak no. 70, as per Map 23 of Village Bedpur Pangana & Tehsil Roorkee, Distt-Haridwar. '},{'Property B:':'Land area measuring 0.309 Hectare (new khasra no. 333), bearing proposed Gata Number 157/3, 160 and 170 area measuring 0.020, 0.013 and 0.276 Hectare, Total area measuring 0.309 Hectare of Chak no. 70, as per map number 23 of village Bedpur- Pargana & Tehsil Roorkee, Distt-Haridwar.'},{'Belonging to:':'Din Dayal Educational Trust (DDS Educational Trust) having its office at 18/1 Idgah, Prakash Nagar Distt-Dehradun through its Joint Secretary Sh. Ankur Sharma S/o Sh. Din Dayal Sharma R/o 18/1 Idgah, Prakash Nagar Distt- Dehradun.(Note- for actual boundaries, kindly refer valuation report.)'}]
date = "10/09/2022"
proposal_no = "82245632"
applicant_name = "DIN DAYAL SHARMA EDUCATIONAL TRUST"
bank_name = "HDFC Bank Dehradun (EEG)"
vendor = "124489"
pan = "APZPS6066C"
gst_line = "(HDFC Bank GST for UK- 05AAACH2702H1Z6)"
hsn = "998214"
whomto = "HDFC Bank Dehradun (EEG)"


doc = DocxTemplate("template.docx")

context = {
    'bill_no': '289/2022-23',
    'sentence_list': sentence_list,
    'proposal_no':proposal_no,
    'applicant_name':applicant_name,
    'date':date,
    'bank_name':bank_name,
    'pan':pan,
    'vendor':vendor,
    'gst_line':gst_line,
    'hsn':hsn,
    'whomto':whomto
}

# Replace the placeholders in the template with the context variables
doc.render(context)

# Save the resulting document
doc.save("output.docx")