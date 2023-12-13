# TrafikverketTrackSwitch

Projekt för att ta fram relevant statistik om Trafikverkets 46k+ växlar

## Fynd
* Trafikverket har otroligt dålig data om sina växlar. 
  * Tex saknar 96% av posterna inkopplingsdatum. 
  * Många saknar inläggningsår. 
  * Många saknar effekt, det är inte tydligt när posterna saknar data eller tex inte har installerat effekt.
* Trafikverket har ingen API eller öppna data om störningar per växel, 
det är en allvarlig brist för det gör det omöjligt att uppskatta vad växelfel beror på för en utomstående. Beror 
det tex på för liten effekt? Gammal hårdvara som slitits bortom planerad livsålder? Eller något annat?

Med det underlag Trafikverket delar idag är det omöjligt för en utomstående att bilda sig en uppfattning om hur 
läget är med växlarna som idag finns inkopplade på svenska järnvägar. Det saknas helt rotfelsanalys både på 
systemnivå, per bana, och per incident)

Jag undrar om Regeringen gett Trafikverket i uppdrag att dela sådan data. Om inte, så kanske det är dags? 

## Bakrund
* Växlarna orsakar ofta stopp i tågtrafiken på vintern
* Tågbolagen är inte nöjda med hur järnvägen sköts för 90% (SJs Årsredovisning 2022) av 
alla störningar är pga infrastrukturproblem som gissningsvis till största del 
kunde ha undvikits om Trafikverket klarade av sitt uppdrag.

## Vad jag lärde mig
* Jag blev lite vassare på GeoPandas tack vara förslag på kod från chatgpt och lite sökningar på nätet
