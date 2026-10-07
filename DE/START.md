# Alte Fotos selbst kolorieren — eigene Übung

## 1. Was dieser Download enthält
Ein eigenes synthetisches, visuell monochromes Übungsfoto, einen kleinen achtteiligen ComfyUI-Workflow, denselben Graphen als API-Prompt, den genauen Prompt und ein leeres Prüfprotokoll. Keine Modellgewichte. Keine neue Installation oder echte lokale Kolorierung als bereits durchgeführt behauptet. Das Bild ist erfunden und kein authentisches Familien-/Archivfoto; leichte RGB-Abweichungen sind in HERKUNFT.json dokumentiert.

## 2. Vorhandene Einrichtung prüfen
Benutze eine bereits funktionierende ComfyUI-Installation mit TextEncodeQwenImage21 und den drei exakt passenden vorhandenen Modellbestandteilen. Fehlende Nodes oder Dateien sind ein echter Blocker. Nicht ähnlich benannte Modelle aus anderen Familien einsetzen. Vor einem Modelllauf andere Arbeit auf demselben Gerät berücksichtigen. Keine automatischen Downloads durch dieses Paket.

## 3. Die UI-Datei öffnen
Alle Dateien in einen neuen Ordner entpacken. Ziehe QWEN21-KOLORIEREN-WORKFLOW.json in die ComfyUI-Arbeitsfläche oder benutze Öffnen. Diese Datei hat nodes/links und Positionen. QWEN21-KOLORIEREN-API.json ist dagegen für /prompt, nicht zum Ziehen in die UI bestimmt. Reale Import-/Inferenzabnahme dieses neuen kleinen Graphen bleibt offen; bei Fehlermeldung nicht einfach weitermachen.

## 4. Eigene Eingabe auswählen
Im LoadImage-Knoten Bild hochladen anklicken und EIGENES-SYNTHETISCHES-FOTO-SW.png aus dem entpackten Ordner wählen. Vorschau kontrollieren und den tatsächlich gespeicherten Dateinamen beachten; ComfyUI kann bei einem vorhandenen Namen einen Zusatz vergeben. Das echte Ausgangsbild erhalten und nicht überschreiben. Später eigene freigegebene Bilder separat ausprobieren.

## 5. Drei Loader einstellen
UNETLoader: qwen_image_2.1_int8_convrot.safetensors. CLIPLoader: qwen3vl_8b_int8_convrot.safetensors, Typ qwen_image. VAELoader: qwen_image_2.1_vae_bf16.safetensors. Das sind Variantenamen des erhaltenen eigenen Bestands, keine automatische Garantie für andere Geräte. Der kleine Graph benötigt keinen Prompt-Enhancer und keinen zusätzlichen Cache-Knoten.

## 6. Leitungen verstehen
Bild → TextEncodeQwenImage21 images.image_1. CLIP → clip. VAE → vae und VAEDecode. Die drei Encoder-Ausgänge positive, negative und latent gehen zu den gleich benannten KSampler-Eingängen. UNET MODEL geht zum KSampler. KSampler LATENT → VAEDecode samples → SaveImage images. Zehn Verbindungen insgesamt. Ein Bild muss wirklich am Encoder hängen.

## 7. Prompt und erster Einzelversuch
PROMPT.txt wortgleich verwenden. Er fordert zurückhaltende Farben und unveränderte Identität, Hände und Komposition; das ist eine Anweisung, keine garantierte Pixel-/Gesichtstreue. Startwerte: Seed11, fixed,25Schritte, CFG1, Euler/simple, denoise1, resolution1024. resolution ist ein Flächenbudget mit erhaltener Eingabeseitenrelation, nicht zwingend ein1024×1024Ausgabebild. Genau einen Lauf in eine freie Warteschlange geben.

## 8. Erfolg erst am neuen Bild prüfen
Queue/Fehler ansehen, den neuen Dateinamen und die aktuelle Ausgabe kontrollieren. API-Annahme oder grüne Queue allein beweisen keine Kolorierung. Ein altes sichtbares Ergebnis kann von einem früheren Lauf stammen. Original und wirklich neue Ausgabe groß nebeneinander ansehen: Augen, Mund, Hände, Knöpfe, Blumen und Bildausschnitt. Farbauftrag und erhaltene Details separat bewerten.

## 9. Ergebnis erhalten und behutsam verbessern
Neues Bild unter eigenem Namen speichern. Fülle DEIN-KOLORIERTEST.csv aus. Bei zu schwacher Farbe Prompt gezielt präzisieren; bei Gesichtsveränderung Ergebnis verwerfen oder eine separate nachgeprüfte Masken-/Rückkomposition verwenden. Seed22 ist eine zweite Variante, keine stillschweigende Verbesserung desselben Versuchs. Eine andere Schrittzahl getrennt protokollieren.

## 10. Geräte und Grenzen
Der Workflow ist nicht pauschal für jede AMD-Grafikkarte, jeden Mac oder12GB-VRAM freigegeben. Einrichtung, Backend, Quantisierung und Speicher entscheiden; die neuen Gerätevarianten wurden nicht praktisch getestet. Ein Speicherfehler bei einem großen anderen Modell beweist nichts über jede Konfiguration. Beginne mit deinem vorhandenen funktionierenden System. Keine historische Farbwahrheit oder Wiederherstellung verlorener Details versprechen.

## 11. Optionaler Offline-Dateicheck
Mit vorhandenem Python: python ./PRUEFE-WORKFLOW.py --folder . --output ./mein-workflowcheck.json . Der Prüfer liest nur Graph, Modellnamen, Leitungen und eigene Eingabe-Hashwerte. Er kontaktiert keinen Server, installiert nichts und startet keine Inferenz. Ein bestandenes Strukturergebnis ersetzt keinen realen UI-/Modelllauf.
