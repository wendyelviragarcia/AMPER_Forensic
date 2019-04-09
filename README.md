# AMPER_Forensic
This tool is designed to create a phonetic profile of an unknown speaker based on his/her intonation. By using Pearson’s correlation, a Python script compares the intonation of an utterance produced by an unknown speaker with the patterns of utterances produced by known speakers. The script suggests a series of geo-prosodic affiliations for the unknown speaker, arranged in order of likelihood. AMPER_Forensic has been tested with AMPER data from Italian, Friulan and Catalan with promising results

### Input
A folder with all the AMPER pitch files (txt in St) that you use as db. Your files must be in '../DBase_Amper_Forensic'

### Output 
Simmilarity matrices and best candidate. Results are saved at: 'resultsForensic/'
