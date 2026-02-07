

from dotenv import load_dotenv
import os
from transformers import logging
logging.set_verbosity_error()
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


load_dotenv()
model_name = os.getenv("MODEL_NAME", "ziaulkarim245/bart-large-cnn-Text-Summarizer")
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

def summarize_text(text: str, max_new_tokens: int = 10000, min_length: int = 25) -> str:
    inputs = tokenizer(text, return_tensors="pt", truncation=True)
    outputs = model.generate(
        **inputs,
        max_new_tokens=max_new_tokens,
        min_length=min_length,
        do_sample=False,
        forced_bos_token_id=0
    )
    summary = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return summary.strip()

if __name__ == "__main__":
    test_text = """Het olympisch kwalificatietoernooi in Thialf is bijna ten einde. Wie gaan in februari naar de Olympische Spelen in Milaan en Cortina d'Ampezzo. Bekijk hier het schema, de selectievolgorde en de uitslagen.
Selectievolgorde


Programma
Dinsdag 30 december
18.58 uur: 1.500 meter mannen

Uitslagen
1.000 meter vrouwen
1. Femke Kok - 1.14,08
2. Suzanne Schulting - 1.14,71
3. Naomi Verkerk - 1.14,74*

*Jutta Leerdam kwam op de 1.000 meter ten val en moet hopen op een aanwijsplek van de KNSB. Een eventuele aanwijsplek van Leerdam zal ten koste gaan van Verkerk.

5.000 meter mannen
1. Stijn van de Bunt - 6.09,30
2. Chris Huizinga - 6.12,10
3. Marcel Bosker - 6.13,10

500 meter mannen
1. Jenning de Boo - 33,96
2. Sebas Diniz - 34,45
3. Joep Wennemars 34,48

3.000 meter vrouwen
1. Marijke Groenewoud - 3.54,73
2. Joy Beune - 3.56,80
3. Merel Conijn - 3.57,36

500 meter vrouwen
1. Femke Kok - 36,87 (baanrecord)
2. Jutta Leerdam - 37,24
3. Anna Boersma - 37,27

10.000 meter mannen
1. Stijn van de Bunt - 12.36,35
2. Jorrit Bergsma - 12.45,52
3. Marcel Bosker - 12.45,98

1.500 meter vrouwen
1. Antoinette Rijpma-de Jong - 1.53,02
2. Femke Kok - 1.53,03
3. Marijke Groenewoud - 1.53,05

1.000 meter mannen
1. Jenning de Boo - 1.06,84
2. Joep Wennemars - 1.07,34
3. Kjeld Nuis - 1.07,541
4. Tim Prins - 1.07,546

5.000 meter vrouwen
1. Merel Conijn - 6.43,46
2. Bente Kerkhoff - 6.46,72

Wat staat er op het spel?
In de basis zijn de regels voor het olympisch kwalificatietoernooi (OKT) simpel. De uitslagen van de races in Thialf bepalen welke Nederlandse schaatsers naar de Olympische Winterspelen (6-22 februari) mogen. Op alle individuele afstanden, behalve op de 5 kilometer voor vrouwen en de 10 kilometer voor mannen, heeft Nederland drie startplekken in Milaan.

Toch is het niet zo dat de top drie per afstand meteen zeker is van een olympisch ticket. Dat komt doordat er maximaal negen mannen en negen vrouwen uit Nederland mogen meedoen aan het olympische schaatsen in Milaan.

Het zou zomaar kunnen dat bij het OKT meer dan negen verschillende mannen of vrouwen in een top drie van een afstand eindigen. Daarom is er een zogenaamde selectievolgorde gemaakt. Op deze lijst staan alle individuele startplekken gerangschikt, van één tot en met vijftien. Tijdens het OKT kan de selectievolgorde worden ingevuld. Zo rolt er uiteindelijk een olympische selectie uit.

Daarbij moet wel worden opgemerkt dat de selectiecommissie van schaatsbond KNSB zowel bij de mannen als bij de vrouwen drie aanwijsplekken achter de hand heeft. Die kunnen worden ingezet als een topper zich door pech (bijvoorbeeld een val of een blessure) niet heeft gekwalificeerd bij het OKT.

De aanwijsplekken kunnen ook worden gebruikt voor de ploegenachtervolging en de massastart. Voor die teamonderdelen verloopt de olympische kwalificatie niet via het OKT. Bondscoach Rintje Ritsma heeft een stem in de selectie, al geeft de selectiecommissie uiteindelijk de doorslag.

Bekijk hieronder de selectievolgorde bij de mannen én de vrouwen.
    """
   
    print("Original Text:", test_text)
    print("Summary:", summarize_text(test_text))