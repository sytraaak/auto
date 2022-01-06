seznam = {"fq":"""
    Oceňování rezervací - H/FQ<br>
    Po ocenění rezervace je nutné mít uloženou masku buď G (guaranteed) nebo A (private fare)<br>
    FQ – fare quote - ocení rezervaci k dnešnímu datu nejlevnějším tarifem v dané třídě<br>
    - F*Q (pouze v návaznosti na jakékoli FQ) – zobrazí detaily ocenění<br>
    FQA – fare quote alternative - zobrazí čtyři varianty ocenění k dané rezervaci<br>
    - FF1 (pouze v návaznosti  na FQA) – uloží tarif z prvního řádku ve FQA<br>
    FQBB – fare quote best buy – ocení rezervaci nejlevnější možnou cenou<br>
    - FQBBK – fare quote best buy confirm - uloží ocenění do rezervace<br>
    FQBB/FXD – ocení rezervaci nejnižší dostupnou třídou se zavazadlem (nemusí být funkční u všech rezervací)<br>
    FQBB++-BUSNS – fare quote best buy business – ocení rezervaci nejlevnějším business třídou<br>
    - PREME = premium economy, FIRST = první třída<br>
    FQ.T20MAY18 – ocení rezervaci k určitému datu<br>
    FQ@GRDCZ9 – protlačení tarifu s názvem GRDCZ9 na celou rezervaci<br> 
    FQ:N – ocenění pouze publikovanými tarify<br>
    FQ:P – ocenění pouze privánítmi tarify<br>
    FQ:EUR - ocenění v EUR (možno použít jakoukoli jinou měnu)<br>
    FQ/CBA – ocení rezervaci s validačním dopravcem British Airways (BA)<br>
    FQP1 – ocenění pouze prvního cestujícího<br>
    FQP1*YTH – ocenění prvního cestujícího jako mládežníka (CNN = dítě, ADT = dospělý, STU = student)<br>
    FQP1*C08/ACC – ocenění prvního cestujícího jako osmileté doprovázené dítě<br>
    FQP1-4 – ocenění prvního až čtvrtého cestujícího<br>
    FQP1.4 – ocenění prvního a čtvrtého<br>
    FQS1/P1 – ocenění pouze první segment pro prvního cestujícího<br>
    FQS1.4/P1 – ocenění prvního cestujícího na segmentu 1 a 4<br>
    FQP1.4/S1-2 – ocenění prvního a čtvrtého cestujícího na segmentu 1 až 2<br>
    FQP1S1@GRDCZ9 – ocenění prvního cestujícího na segmentu jedna tarifem GRDCZ9<br>
    FQS1@GRDCZ9/S2@T3WKCZ9/P1 – ocenění prvního cestujícího na segmentu číslo jedna tarifem  GRDCZ9 a na segmentu číslo 2  T3WKCZ9<br>
    FQS1@GRDCZ9/S2@T3WKCZ9/P1.T20MAY18 – ocenění prvního cestujícího na segmentu číslo jedna tarifem GRDCZ9 a na segmentu číslo 2  T3WKCZ9 k datu 20.5.2018<br>
    FQS1.3@THWNCT8/MB2/P5 – ocenění patého cestujího na prvním a třetím segmentu tarifem  THWNCT8 při openjaw letence, kdy je pozemní segment na druhém segmentu (MB = must break)<br>
    FQP1*CMA/P2*CMP - ocenění pro companion tarif (tarif pro dva a více cestující) <br>
    FQP1*ITX:P - ocenění TO tarifem pro dospělého pasažéra 1 <br>
    FQP2*I08/ACCITX:P - ocenění TO tarifem pro dítě ve věku 8 let - pasažér 2<br> 
    FQP3*ITF/ACCITX:P - ocenění TO tarifem pro infanta - pasažér 3 """,
          "fd":"""
    Fare display - H/FD<br>
    FD15AUGPRGCDG – zobrazí všechny tarify na trase z Prahy do Paříže pro všechny dopravce<br>
    FD15AUGPRGCDG:P – vyhledá pouze privátní tarify (:N - publikované) <br>
    FD15AUGPRGCDG/AF – zobrazí všechny tarify na trase z Prahy do Paříže  s Air France<br>
    FD15AUGPRGCDG/AF/OK/QS – zobrazí všechny tarify na trase PRG – CDG s AF + OK + QS<br>
    FD15AUGPRGCDG/AF/OK/QS@Y - vyhledá economy tarify (W = premium, C = business, F = first)<br>
    FD15AUGPRGCDG/AF/OK/QS-RT – zpáteční tarify na trase PRG – CDG s AF + OK + QS <br>
    FD15AUGPRGCDG/AF/OK/QS-OW - jednosměrné tarify na trase PRG – CDG s AF + OK + QS<br>
    FD15AUGPRGCDG/AF-OW-K - jednosměrné tarify v třídě K<br>
    FD15AUGPRGCDG/AF-OW-K.T20MAY18 – tarify k datu 20.5.2018<br>
    FD15AUGPRGCDG/AF-OW-K.T20MAY18*YTH – mládežnické tarify (CNN = dítě, INF = infant, STU = student, SRC = senior)<br>
    FD15AUG17PRGCDG/AF-OW-K.T20MAY17*YTH – historické zobrazení ceníku k datu vystavení 20.5.2017 s datem odletu 15.8.2017<br>
    FD15AUGPRGCDG/AA-RT-O/L – zobrazí tarify v třídě O pro všechny sezóny<br>
    FDPRGGYD04MAR/J2::USD - některé letecké společnosti loadují i tarify z Prahy v jiné měně, než CZK - ty si zobrazíme vsupem <br>
    FDPRGFRA10JUN/OK-PRI-KOR:P – zobrazí se korporátní tarify letecké společnosti ČSA s odletem 10.6. na trase Praha – Frankfurt pro firmu s kódem KOR a popřípadě další privátní tarify (např pokud má letecká společnost jako privátní tarify označené tarify bez zavazadla - Finnair atd.)<br> 
    FDPRGFRA10JUN/OK-PRI-KOR – zobrazí se všechny publikované a také korporátní tarify letecké společnosti ČSA s odletem 10.6. na trase Praha – Frankfurt pro firmu s kódem KOR. <br>
    FDPRGFRA10JUN/OK-PRI-:KOR – zobrazí se pouze korporátní tarify letecké společnosti ČSA s odletem 10.6. na trase Praha – Frankfurt pro firmu s kódem KOR FDPRGFRA10JU-PRI-KORPOMASTER - zobrazí se<br> 
    FDPRGFRA10JUN-PRI-KORPOMASTER - zobrazí se korporátní tarify všech letckých společností, které firmě poskytly korporátní tarify na trase Praha – Frankfurt. Firma musí mít v HEO uvedem tzv. Mastercode. """,
          "fs":"""
    Focal shopping - H/FS<br>
    FSLON10JANDXB - vyhledá jednosměrnou letenku na 10JAN z LON do DXB<br>
    FS2FRA10JUNLON  - dva cestující, zpáteční letenka<br>
    FS2FRA10JUNLON17JUNFRA+P1.2*C07  - dva cestující - dospělý + dítě ve věku sedmi let<br>
    FSLON10JANDXB20JANLON - zpáteční letenka na 10JAN z LON do DXB a 20JAN zpět<br>
    FS2PRG10SEPNYC20SEPPRG+FXD - vyhledá letenku se zavazadlem (raději vždy kontrolujte)<br>
    FSBKK11JUNHKG17JUNSIN20JUNTYO25JUNBKK - circle trip<br>
    FSLON10JANDXB--AUH20JANLON - OPEN JAW -- se dává v bodě, kde je pozemní sektor<br>
    FSFRA10JUNLON17JUNFRA+*C10 - specifický kód cestujícího<br>
    FSIEV01DECROM18DECIEV+*YTH - definování podle kódu pasažéra (PTC)<br>
    FS3FRA10JUNLON17JUNFRA+P1-2.3*C10.4*INF - vyhledávání pro dva dospělé cestující, desetileté dítě a infanta (pozor na počet míst, infant se nepočítá)<br>
    FSVIE10JUNCDG15JUNVIE/AF - preferovaný dopravce <br>
    FS3FRA10JUNLON17JUNFRA+P1-2.3*C10.4*INF/AF - kombinace předchozích vstupů<br> 
    FSSIN11JUNHKG-BUSNS - preferovaná kabina business (možno použít FIRST nebo PREME)
    <center><b><u>Výsledky focal shopping</b></u>
    <center><img src="static/img/fs.png"></center> 
    """
          }
