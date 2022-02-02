from time import sleep
import sys
import time
import os
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.12)
    print("")
    sleep(0.5)
#delay_print("I want this text big")
clear = lambda: os.system('cls') #on Windows System
clear()
police=False
mom=False
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
title='INSANITY'.center(150)
print(title)
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
delay_print("Witaj przyjacielu oto moja gra INSANITY cz.I Czy chcesz zagrać?")



answer = input("tak/nie: ").lower()
if answer == "tak":
    clear()
    text = "dobry wybór".upper()
    print(text)
    sleep(1)
    delay_print("Witaj w grze w której zmierzysz się ze swoim odwiecznym lękiem. Nie jest to gra dla ludzi o słabych nerwach.")
    print("")
    sleep(1)
    delay_print("Dla lepszego komfortu gry zalecam zgasić światła i wyłączyć telefon oraz inne urządzenia oraz zapuścić na słuchawkach"
                ": https://youtu.be/k68thGEDlx8ok")
    print("Masz teraz czas na te czynności.")
    answer = input("Jezeli jestes gotowy potwierdz wpisujac ok: ").lower()
    name = input("Abyśmy mogli zacząć podaj jeszcze swoje imię: ").capitalize()
    if answer == "ok":
        sleep(2)
        clear()
        text=("A więc wybrałeś śmierć "+name).upper().center(150)
        print(text)
        sleep(3)
        while True:
            clear()
            print("O BOŻE")
            sleep(1)
            delay_print("Zdyszany budzisz się w swoim łóżku.")

            delay_print("Miałeś koszmarny sen tej nocy. Myślałeś że ktoś cię goni a ty z całych sił próbujesz mu uciec. Jesteś cały zalany potem")

            sleep(0.5)
            delay_print("Zza okna dostrzegasz, że wciąż panuje półmrok")

            sleep(0.5)
            print("Ciemny")
            sleep(0.5)
            print("Nieprzenikniony")
            sleep(1)
            print("MROK")
            sleep(2)
            delay_print("Wciąż lekko spocony powoli się uspokajasz. To tylko sen okej. Tylko sen.")

            sleep(1)

            while True:
                answer = input(
                        "Co robisz? A.Kładziesz się i próbujesz zasnąć/ B.Sięgasz po telefon by sprawdzic godzine: ").lower()
                sleep(1)
                clear()
                if answer == "a":
                    delay_print("Muszę się wyspać, jutro mam ważną prezentację. Kładziesz się na łóżko.")
                    sleep(1)
                    print("10 minut")
                    sleep(2)
                    print("20 minut")
                    sleep(3)
                    delay_print("Cholera nie mogę zasnąć. W dodatku mam sucho w ustach. Muszę iść do kuchni po wodę. Wstajesz z łożka.")
                    break
                elif answer == "b":
                    delay_print("Po omacku wyciągasz rękę po telefon znajdujący się na parapecie")
                    delay_print("Próbując złapać telefon czujesz że coś delikatnie potarło cię o łokieć")
                    delay_print("Ciarki przechodzą cię po całym ciele. Natychmiast zabierasz telefon i świecisz w to miejsce latarką")
                    sleep(1.5)
                    delay_print("Nic tam nie ma to chyba tylko wyobraźnia. Sprawdzasz godzinę. Jest 2:58")
                    delay_print("Od tych wszystkich emocji zachciało ci się pić, więc wstajesz z łóżka aby iść do kuchni po wodę")
                    break
                else:
                    delay_print("wybierz opcję A lub B")
                    clear()


            delay_print("Wszędzie panują ciemności. W mroku próbujesz wymacać włącznik światła.")
            sleep(1.5)
            delay_print("Nie działa. Ostatnio były problemy z dostawami prądu. Bierzesz telefon aby użyć go jako latarki.")
            delay_print("Idąc do kuchni nie możesz pozbyć się dziwnego wrażenia. Ktoś najwyraźniej się tobie przygląda")
            delay_print("Docierasz do kuchni, nalewasz sobie wody do szklanki")
            sleep(2)
            print(name+ "(Coś zaszeleszczało)")
            sleep(1)
            delay_print("Odrwacasz się natychmiast ale nikogo nie ma")
            delay_print("Ktoś wyszeptał moje imię?")
            sleep(0.5)
            delay_print("Chyba mam urojenia.")
            delay_print("Podnosisz szklankę wody do ust")
            sleep(2)
            print(name+"! (Tym razem głośno i wyraźnie)")
            sleep(1)
            delay_print("Na sekundę zamierasz")
            sleep(1)
            delay_print("Nie przesłyszałeś się ")
            delay_print("Ktoś wypowiedział moje imię")
            while True:
                weapon = input("Przerażony chwytasz za A.Nóż kuchenny/B.Kij od szczotki: ").lower()
                clear()

                if weapon == "a":
                    weapon="nóż kuchenny"
                    break
                elif weapon == "b":
                    weapon="kij od szczotki"
                    break
                else:
                    print("Wybierz dostępną opcję")

            delay_print("Ktoś jest w twoim domu. Mieszkasz sam więc ktoś musiał się włamać. Strach zaczyna powoli cię paraliżować")
            delay_print("Co teraz? Ten ktoś jest blisko i zaraz cię dopadnie")
            delay_print("Zauważasz w salonie będącym przedlużeniem kuchni nieznaczny ruch jakiejś ciemnej, smukłej sylwetki")
            answer = input("Co robisz? A.Uciekasz jak najszybciej z mieszkania/B.Podchodzisz by sprawdzić kto(lub co) znajduje się w salonie: ").lower()
            if answer == "a":
                clear()
                delay_print("Trzymając w jednej ręce telefon z latarką a w drugiej "+weapon+" rzucasz się do ucieczki")
                delay_print("Biegniesz z kuchni przez korytarz i wpadasz jak szalony na drzwi wejściowe i zaczynasz szarpać za zamek")
                sleep(2)
                delay_print("to na nic")
                delay_print("Przypomniałeś sobie że zamknąłeś drzwi na dolny zamek a klucze masz w swoim pokoju")
                delay_print("Odwracasz się ale na końcu korytarza jakieś 3 metry od Ciebie stoi...")
                delay_print("On")
                delay_print("A raczej to coś bo napewno nie było to człowiekiem")
                sleep(0.5)
                delay_print("Stworzenie to miało ponad 2 metrów wzrostu, prawie dotykało sufitu")
                delay_print("Jego nienauralnie dłuie ręce zwisały bezwładnie wzdłuż ciała a dłonie leżały na podłodzę ")
                delay_print("Delikatnie kiwał się z jednej strony na drugą i nawet z tej odległości dało się usłyszeć jego sapanie")
                sleep(0.5)
                delay_print("Po krótkiej chwili rozdziawił swoje usta ujawniając tysiące długich i ostrych jak igły zębów")
                delay_print("Ledwie słyszalnym głosem wychrypiał: Witaj "+name+ "! i zaczął powoli kuśtykać w moją stronę")
                delay_print("Wrzeszczałem tak głośno jak tylko potrafiłem ale on cały czas w żółwim tempie zbliżał się do mnie")
                delay_print("Nagle w komórce zgasło światło i wszystko zrobiło się całkowicie ciemne")
                sleep(4)
                continue
            elif answer == "b":
                clear()
                delay_print("Powoli wchodzisz do salonu. Salon jest największym pomieszczeniem w twoim domu")
                delay_print("Panuje tu absolutna ciemność")
                answer = input("A.Krzyczysz / B.Zaczynasz świecić latarką po salonie: ").lower()
                if answer == "a":
                    delay_print("Halo! Kto tu jest! Mam "+weapon+" i nie zawacham się go użyć!")
                    sleep(2)
                    print("cisza")
                sleep(1)
                delay_print("Telefonem który masz w ręce zaczynasz oświetlać pokój")
                delay_print("Duży stół na środku a wokół niego krzesła wyglądają na nietknięte")
                delay_print("Obrazy na ścianie przedstawiające twoich zmarłych członków rodziny przypatrują się tobie jak zawsze")
                delay_print("Przelatując snopem światła dostrzegasz dziwny kształt w rogu pokoju")
                delay_print("Pryglądasz się temu przez chwile")
                delay_print("Wygląda ja ogromna delikatnie kołysząca się sylwetka z nienaturalnie długimi kończynami oraz okrągłą sferą bez wyrażnych szczegółów w miejscu głowy")
                delay_print("Kamieniejesz ze strachu.")
                answer=input("Przez ściśnięte gardło udaje ci się jedynie wypowiedzieć A.Kim jestes?/B.Czego chcesz?").lower()
                if answer=="a":
                    sleep(2)
                    delay_print("Kim jestem? - wychrypiała postać odkrywając rząd długich i ostrych jak sztylety kłów")
                    delay_print("Zaraz się przekonasz. - wykrzywiła usta w dziwnym grymasie przypominającym uśmiech i powli zaczęła kuśtykać w moją stronę")
                elif answer=="b":
                    sleep(2)
                    delay_print("Oooooh - zaskrzypiała postać jakby każde słowo przychodziło jej z jak największym trudem")
                    delay_print("Dostrzegłeś w jej paszczy rzędy ostrych i długich kłów przypominających kolce")
                    delay_print("Chce się tylko dobrze zabawić. - powiedziała wykrzywiła usta w dziwnym grymasie przypominającym uśmiech i powli zaczęła kuśtykać w moją stronę")
            sleep(1)
            delay_print("Wiedziałeś, że "+weapon+ " na niewiele się zda")
            delay_print("Musisz uciekać jak najszybciej zanim to coś Cię dopadnie")
            while True:
                clear()
                answer=input("A.Uciekasz do drzwi wejściowych aby wybiec na ulice/B.Zbiegasz po schodach do garażu/C.Uciekasz do pokoju się zabarykadować: ").lower()

                if answer == "a":
                    delay_print("Uciekasz ile sił nogach. Wpadasz z hukiem na drzwi wejściowe.")
                    delay_print("Szybko odbezpieczasz zamki i zaczynasz szarpać za klamkę z całej siły ")
                    delay_print("Drzwi ani drgną")
                    delay_print("Przypomniałeś sobie że zakluczyłeś drzwi na dolny zamek a klucze masz w swoim pokoju")
                    delay_print("Odwracasz się ale na końcu korytarza jakieś 3 metry od Ciebie stoi On")
                    delay_print("A raczej to coś bo napewno nie było to człowiekiem")
                    sleep(0.5)
                    delay_print("Stworzenie to miało ponad 2 metrów wzrostu, prawie dotykało sufitu")
                    delay_print("Jego nienauralnie dłuie ręce zwisały bezwładnie wzdłuż ciała a dłonie leżały na podłodzę ")
                    delay_print(
                        "Delikatnie kiwał się z jednej strony na drugą i nawet z tej odległości dało się usłyszeć jego sapanie")
                    sleep(0.5)
                    delay_print(
                        "Po krótkiej chwili rozdziawił swoje usta ujawniając tysiące długich i ostrych jak igły zębów")
                    delay_print(
                        "Ledwie słyszalnym głosem wychrypiał: Witaj " + name + " i zaczął powoli kuśtykać w moją stronę")
                    delay_print(
                        "Wrzeszczałem tak głośno jak tylko potrafiłem ale on cały czas w żółwim tempie zbliżał się do mnie")
                    delay_print("Nagle w komórce zgasło światło ponieważ padła bateria i wszystko zrobiło się całkowicie ciemne")
                    sleep(4)
                    clear()
                    continue

                elif answer=="b":
                    delay_print("Uciekasz ile sił w nogach w stronę najbliższych drzwi. Prowadzą one do zagraconego pomieszczenia gospodarczego")
                    delay_print("Potykasz sie o karton z ksiązkami i lądujesz na podłodze. Szybko otrzepujesz się i wstajesz.")
                    delay_print("Updając poraniłeś się i leci Ci krew ale jesteś tak spanikowany i przerażony, że nawet nie czujesz bólu")
                    delay_print("Kątem oka zauważasz że to cholerstwo cały czas zbliża się w twoją stroną swoim powolnym, wykoślawionym krokiem")
                    delay_print("Dopadasz czym prędzej do drzwi prowdzących do garażu")
                    delay_print("Stoi tam twój samochód do którego wsiadasz najszybciej jak potrafisz. Wcześniej jeszcze otwierasz bramę od garażu aby jak najszybciej uciec")
                    delay_print("Uffff. Kluczyk w stacyjce co za ulga. Przekręcasz go.")
                    sleep(1)
                    delay_print("Co jest kurwa!")
                    print("Raz")
                    sleep(1)
                    print("Drugi")
                    sleep(1)
                    print("Trzeci")
                    sleep(1)
                    delay_print("Nie działa! Stacyjka pokazuje, że akumulator się rozładował. Zostawiłeś włączone światła na całą noc.")
                    delay_print("Kątem oka widzisz jak drzwi od garażu się zaczynają uchylać a do środka wślizguje się powoli długa powyginana czarna ręka.")
                    delay_print("Nie ma czasu musisz wiać!")
                    delay_print("Wysiadasz z auta i trzymając wciąż w dłoni "+weapon+ ", uderzasz nim w ochydną dłoń za drzwiami")
                    delay_print("W odpowiedzi usłyszałem przerażający, rozdzierający słuch wrzask")
                    delay_print("Wybiegasz czym prędzej na ulicę przez otwartą bramę. ")


                elif answer=="c":
                    delay_print("Uciekasz jak najszybciej do pokoju. Zamykasz drzwi na klucz i przewracasz szafę tak aby je dodatkowo zablokować")
                    delay_print("Skulony czekasz w koncie pokoju.")
                    delay_print("Może sobie pójdzie i da mi spokój.")
                    delay_print("Przez głowę przelatuje ci milion pytań.")
                    delay_print("Czy to się dzieje na prawdę? Czy ja nadal śnię?")
                    delay_print("Rozmyslania przerywa potężny huk w twoje drzwi. Był tak mocny że szafa odsunęła sie o pare centymetrów a drewniane drzwi popękały w paru miejscach.")
                    delay_print("Zaczynasz wrzeszczeć najgłośniej jak potrafisz. Myślisz że za chwilę zemdlejesz z przerażenia")
                    delay_print("Kolejne potężne uderzenie roztrzaskuje drzwi na kawałki i do środka wdziera się potężna, ciemna i przerażająca postać")
                    delay_print("Jej potężne kły lśnią w świetle księżyca zza okna.")
                    delay_print("Okno? No właśnie! Może uda mi sie szybko przez nie wybiec.")
                    while True:

                        answer=input("A.Podejmujesz walkę z potworem/B.Próbujesz wyskoczyć przez okno: ").lower()
                        clear()
                        if answer == "a":
                            delay_print("W akcie desperacji nacierasz na bestię trzymając "+weapon+" w ręce")
                            delay_print("Zanim jednak udaje ci sie wyprowadzić cios jego długie i powykręcane ręce łapią cię za ramiona i rozrywają z łatwością jak szmacianą lalkę")
                            delay_print("Krew i flaki rozbryzgują się po całym pokoju")
                            sleep(5)
                            continue
                        elif answer == "b":
                            delay_print("Trzymając w dłoni "+weapon+" uderzasz z całej siły w okno. Pojawiły się pęknięcia ale okno nie pękło.")
                            delay_print("Kurwa mać to coś jest coraz bliżej!")
                            delay_print("Bierzesz rozbieg i z całej siły wpadasz na okno taranując szybę i wypadając na zewnątrz")
                            delay_print("Boli potwornie. Odłamki wbiły ci się w każde miejsce w ciele. Jednak strach sprawia że natychmiast się podnosisz i zaczynasz uciekać.")
                            break
                        else:
                            print("Wybierz jedną z dostępnych opcji")

                else:
                    print("Wybierz dostępną opcje")
                delay_print(
                    " Biegniesz tak szybko i długo jak nigdy nie oglądając się za siebie.")
                delay_print("Dopiero parę ulic dalej stajesz i padasz na krawężnik wycieńczony")
                delay_print("Leżąc tak pojawia Ci sie przed oczami obraz wielkiego miasta z gigantycznymi wieżowcami i latającymi samochodami.")
                answer = input("A.Wstajesz i próbujesz się z kimś skontaktować/B.Leżysz i majaczysz dalej: ").lower()
                clear()
                while True:
                    if answer == "a":
                        delay_print("Musisz otrząsnąć się z tego szoku. Wciąż cały drżąc powoli wstajesz na nogi.")
                        break
                    elif answer=="b":
                        delay_print("Marzysz dalej. Przewijają Ci się przez myśli różne obrazy trwające niedłużej niż sekundę.")
                        delay_print("Pełną widownię w teatrze. Zakrwawiony nóż. Gwizdy i buczenie...")
                        delay_print(name+" musisz się ocknąć!! - krzyczysz na siebie i wstajesz na nogi")
                        break
                    else:
                        print("wybierz dostępną opcję")
                delay_print("Wyciągasz z kieszeni telefon. Właśnie padła bateria. Nic dziwnego skoro cały czas była włączona latarka")
                delay_print("Patrzysz na niebo.")
                delay_print("Noc dzisiaj wyjątkowo spokojno. A księżyc przeogromny i potwornie jasny")
                delay_print("Myślisz żeby iść na posterunek policji ale przypominasz sobie że twoja mama mieszk niedaleko i musisz ją ostrzec")
                while True:
                    if (police == True) and (mom ==True):
                        answer = input("A.Idziesz na policję/B.Idziesz do mamy/C.Poznaj prawdę: ").lower()
                    else:
                        answer=input("A.Idziesz na policję/B.Idziesz do mamy: ").lower()
                    clear()
                    if answer=="a":
                        police=True
                        delay_print("Jesteś cały poobijany ale z trudem idziesz w stronę najbliższego posterunku")
                        delay_print("Cały czas rozglądasz się czy przerażająca bestia, która cię zaatakowała nie czai się gdzieś w pobliżu")
                        delay_print("Dochodzisz po 20 minutach na posterunek. Na szczęście okazuję się że jest otwarty")
                        delay_print("Wchodzisz do środka. W okienku poczekalni siedzi plecami dyżurny i energicznie macha ręką w górę i w dół")
                        delay_print("Chyba coś ogląda")
                        delay_print("Ekhm Przepraszam - zwracasz na siebie uwagę")
                        delay_print("Wystraszony odwraca się i patrzy na ciebie ze zdenerwowaniem jakbyś co najmniej zabił mu matkę")
                        delay_print("W czym mogę pomóc - wycedza przez zęby wyraźnie niezadowolony")
                        delay_print("Opowiadasz całą historię a posterunkowy słucha jej w milczeniu przytakując")
                        delay_print("Z początku wydawało ci się że weźmie cię za wariata ale on słucha w skupieniu każdego słowa cały czas przytakując")
                        delay_print("Poczekaj chwilę - mówi do ciebie jednocześnie wyciągając telefon i wybirając numer")
                        delay_print("Siadasz w poczekalni podczas gdy on rozmawia z kimś przez telefon")
                        delay_print("Mija ok 15 min a przyjeżdża drugi policjant. Ten wygląda na starszego i znacznie wyższego rangą. Poznajesz to po wielu odznaczeniach na mundurze")
                        delay_print("Coś tu nie gra. Masz złe przeczucia.")

                        while True:
                            answer = input("A.Uciekasz z posterunku jak najszybciej/B.Czekasz na to co się wydarzy: ").lower()
                            clear()
                            if answer == "a":
                                delay_print("Zrywasz się z krzesła i zaczynasz uciekać ale zauważają to mundurowi")
                                break

                            elif answer == "b":
                                delay_print("Pójdziesz ze mną - mówi w końcu do Ciebie wyższy rangą policjant")
                                delay_print("Nie ma mowy nigdzie nie idę z wami! - Nie ufasz policjantowi")
                                delay_print("Nie pytam Cię o zdanie!")
                                delay_print("Pocałujcie mnie obaj w dupę - Wstajesz i wychodzisz")
                                break
                            else:
                                print("wybierz dostępną opcję")
                        delay_print(
                                    "Stój natychmiast! - krzyczy wyższy rangą i wyciąga w twoją stronę pistolet - Ani kroku dalej!")
                        delay_print(
                                    "Zastygasz w miejscu. Widzisz tylko wycelowaną lufę w swoją twarz. Wiesz że nie zawacha się oddać strzału")
                        delay_print(
                                    "Wiem, że prawda może być dla Ciebie trudna ale musimy ci to pokazać - powiedział kompletnie zmieniajac ton i opuszczajac pistolet")

                        delay_print("Co tu się dzieje? Kim jesteście? Czym jest ten potwór, ktory o mało mnie nie zabił? - krzyczysz tłumiąc płacz")
                        delay_print("Chodź za mną "+name+" wszystkiego się dowiesz - powiedział mundurowy")
                        delay_print("Skąd on zna twoję imię? Nie masz innego wyjścia, jeśli spróbowałbyś uciec na pewno bez wachania by cię zastrzelił")
                        delay_print("Przechodzisz za nim przez pierwsze drzwi a za wami wchodzi policjant z którym rozmawiałeś na początku. Widzisz jak zamyka drzwi na klucz.")
                        delay_print("Czujesz gigantyczny niepokój tym co za chwile nastąpi ale nie masz innego wyjścia. Nie widzisz żadnej drogi ucieczki")
                        delay_print("Jeżeli spróbujesz jakichś sztuczek to podziurawię cię jak ser - syknął policjant idący za tobą")
                        delay_print("Schodzicie gdzieś w dół po mentalowych krętych schodach. Coraz niżej aż w końcu dochodzicie do wąskiego korytarza")
                        delay_print("Na końcu ciemnego korytarza dostrzegłeś święcący punkt")
                        delay_print("Co tam jest? - pytasz policjanta")

                        delay_print("Za chwilę sam zobaczysz - odpowiedział. W miarę zbliżania się do końca korytarza światło stawało sie coraz jaśniejsze i coraz mocniej dało słyszeć sie dudnienie")
                        delay_print("Nie... To okrzyki ludzi. Coraz lepiej i głośniej słyszalne")
                        delay_print("Dotarliśmy do końca korytarza. Znajdowała się tu kurtyna zza której bił ten blask. Teraz było tak jasne, że oślepiające, a krzyk zza drzwi ogłuszająco głośny")
                        delay_print("Policjant gestem ręki nakazał Ci przejść przez kurtynę. Zrobiłeś to co kazał... Natychmiast zostałeś oślepiony ogromnym snopem światłą i ogłuszony ludzmimi odgłosami")
                        delay_print("Po chwili twoje oczy przyzwyczajają się do światła i zauważasz że stoisz na scenie. A naprzeciwko Ciebie aplauzująca widownia")
                        delay_print("Ogromna widownia, wysoka chyba na chyba kilkaset rzędów, może mierzyć nawet ze 100 metrów wysokości. A na niej tysiące ludzi wpatrzonych w ciebie. ")
                        delay_print("Rozglądasz się dookoła i dostrzegasz taką widownię z każdej strony. Przypomina to stadion. Tylko nigdy nie widziałeś tak gigantyczego stadionu")
                        delay_print("Patrzysz w górę a tam ponad wszystkich głowami dziesiątki ekranów. Na każdym z nich co innego. Twój pokój. Twoja kuchnia. Dom twojej matki. Posterunek policji.")
                        delay_print("Zaczyna robić Ci się słabo. Co to jest do cholery? To nie może być prawda ")
                        answer = input("A.Zaczynasz bić się próbując się obudzić/B.Zaczynasz krzyczeć: ").lower()
                        clear()
                        if answer == "a":
                            delay_print("To musi być sen. Bardzo realistyczny ale to nie może być prawda.")
                            delay_print("Zaczynasz okładać się pięściami z całej siły. Boli ale masz nadzieje że wszystko to zniknie. Okaże się tylko iluzja")
                            delay_print("Kładziesz się na ziemii i zaczynasz się tarzać, płacząc jednocześnie. Nie masz już siły nawet na jakikolwiek ruch")

                        elif answer == "b":
                            delay_print("Co to kurwa jest?! Gdzie ja jestem? Jaja sobie ze mnie robicie? - wrzeszczysz ")
                            delay_print("Wycieńczony upadasz na czarny wyszlifowany parkiet na którym się znajdujesz. Nie masz nawet siły na płacz")


                        delay_print("Wszystkie te działania skutkują tylko wzmożonym wiwatem i okrzykami na widowni.")
                        delay_print("Ludzie pokazują palcami na ciebie śmiejąc się i skandując "+name+"!..."+name+"!")
                        delay_print("Wszystko się rozmazuje się, okrzyki giną gdzieś we mgle")
                        delay_print("Ostatnie co widzisz to policjanci podoszący Cię z podłogi. Następnie odpływasz.")
                        sleep(4)
                        continue
                    elif answer == "b":
                        mom = True
                        delay_print("Muszę najpierw iść do mamy. Zobaczyć czy wszystko z nią w porządku - myślisz. Ona jest dla Ciebie wszystkim. Całą rodziną.")
                        delay_print("Nie masz nikogo bliskiego poza nią. Gdyby coś jej się stało twoje życie straciłoby sens.")
                        delay_print("Jej mieszkanie jest niedaleko. Dosłownie parę ulic stąd. Jesteś cały obolały i zmęczony ale z trudem idziesz.")
                        delay_print("Dla swojej matki zrobiłbyś wszystko. Idąc rozmyślasz o tym jak zawsze Cię wspierała i pomagała Ci.")
                        delay_print("Specjalnie wzięła nawet kredyt na siebie żeby opłacić twoje mieszkanie. Do oczu napływają Ci łzy na myśl o tym że coś złego mogło się stać.")
                        delay_print("Cały czas rozglądasz się czy nie ma tego cholernego upiora. Co to mogło być? Może po prostu mam paranoję i postradałem zmysły-myślisz. ")
                        delay_print("Po drugiej stronie ulicy dostrzegasz stację benzynową. Nachodzi cię ochota na szluga.")

                        answer = input("Wpisz 'szlug' jeśli chcesz wejść po papierosy. Jeśli nie wpisz cokolwiek: ").lower()
                        clear()
                        if answer=="szlug":
                            delay_print("Musisz się odstresować i zapalić. To silniejsze od Ciebie. W obliczu tego co się wcześniej wydarzyło może pomoże to zebrać myśli do kupy.")
                            delay_print("Dobry wieczór! - mówisz wchodząc do stacji. Wyraźnie znudzona ekspedientka mruczy coś pod nosem")
                            szlug=input("Poproszę: ")
                            delay_print("Skończyły się "+ szlug+", są tylko LM Niebieskie albo Marlboro Goldy")

                            while True:
                                answer = input("LM/Marlboro: ").lower()
                                clear()
                                if answer == "lm":
                                    szlug = "LMów"
                                    break
                                elif answer == "marlboro":
                                    szlug="Marloboro"
                                    break
                                else:
                                    delay_print("Mówiłąm mamy tylko LM i Marloboro czego nie rozumiesz - zaskrzeczała zdenerwowana kasjerka")
                            delay_print("15,70 poproszę - mruknęła - A co Pan taki poraniony jakby z bijatyki wracał")
                            answer = input("A.Opowiadasz wszystko co się zdarzyło/B.Spławiasz ekspedientkę: ").lower()
                            if answer=="a":
                                delay_print("No no. Niezły z Pana kawalarz- śmieje się pod nosem.")
                                delay_print("Rozwściecza Cię to. Przeszedłem to piekło a ona jeszcze się śmieje!")
                                delay_print("Pierdol się ty głupia dziwko! - krzysz i wychodzisz ze stacji")
                            elif answer=="b":
                                delay_print("Przewróciłem się po prostu - machasz ręką i wychodzisz na zewnątrz")
                            delay_print("Od razu po wyjściu otwierasz paczkę "+szlug+" i mocno się zaciągasz papierosem.")
                            delay_print("O tak. Od razu lepiej. Ale muszę iść jak najszybciej")
                        else:
                            delay_print("Nie mam na to czasu. Muszę szybko tam dojść bo zwariuje - myślisz")
                        delay_print("Po około 10 minutach docierasz do znajomego osiedla. Domki wyglądają tu tak samo ustawione jeden obok drugiego.")
                        delay_print("Jednak ty dobrze wiesz do którego zmierzasz. Zawsze przychodzisz tu w niedzielę na obiad. Twoja kochana mama robi najlepszą zupę pomidorową na świecie")
                        delay_print("Wchodzisz na trawnik. Jest późno więc twoja mama pewnie śpi. Dobrze że znasz kod do drzwi wejściowych.")
                        delay_print("Zbliżasz rękę do klawiatury aby wpisać kod.")
                        delay_print("W tym momencie uderza Cię coś strasznego. Przerażająca myśl, że coś tu jest nie w porządku. Sam nie wiesz dlaczego ale masz bardzo złe przeczucia.")
                        answer = input("A.Wchodzisz do mieszkania/B.Wycofujesz się: ").lower()
                        clear()
                        if answer == "b":
                            delay_print("Coś tu zdecydowanie jest nie tak. Strach wzrasta w Tobie coraz bardziej.")
                            delay_print("Muszę to zrobić. Nie mogę się wycofać z powodu moich chorych jazd. Zobacze tylko czy z mamą wszystko ok i po prostu zawiadomie z jej telefonu policje")
                        delay_print("Nie ma odwrotu")
                        delay_print("Wpisujesz kod. Drzwi otwierają się i wchodzisz do mieszkania. Zamykasz za sobą drzwi.")
                        delay_print("Niepokój wzrasta w Tobie z każdą sekundą. Cały dygoczesz ze strachu. W całym domu panuje nieprzenikniona ciemność.")
                        delay_print("Słyszysz jakieś przytłumione dźwięki. Dochodzą z pokoju telewizyjnego. Przechodzisz przez korytarz, przedpokój i kuchnię")
                        delay_print("Teraz słyszysz dźwięki wyraźniej ale nie na tyle żeby dosłyszeć cokolwiek sensownego. Widzisz też zza szyby poświatę telewizora")
                        delay_print("To niemożliwe! Niemożliwe żeby moja matka oglądała teraz telewizję. Może zapomniała wyłączyć- myślisz sobie chociaż wiesz że to absurd")
                        delay_print("Jak w amoku idziesz w kierunku pokoju, otwierasz drzwi i wchodzisz do środka.")
                        delay_print("Telewizor wyświetla jakiś program przyrodniczy.")
                        delay_print("Naprzeciwko niego, na kanapie siedzi twoja matka. Jej odcięta głowa spoczywa na kolanach a martwe oczy wpatrują się wprost na Ciebie")
                        delay_print("Na ścianie jest napisane krwią: Jesteś mordercą "+name+"!")
                        delay_print("Wymiotujesz. Twoje żygi zalewają twoją koszulkę i buty")
                        delay_print("Czujesz jak wszystkie siły odchodzą i bezwładnie upadasz na kolana")
                        delay_print("Wszystko przed oczami zaczyna Ci ciemnieć. Zaczynasz tracić przytomność. Przed tym słyszysz jeszcze tylko rozdzierający krzyk. ")
                        sleep(2)
                        continue
                    if answer == "c" and (police == True) and (mom ==True):
                        sleep(4)
                        delay_print("Hej, wszystko ok "+name+"?")
                        delay_print("Wyglądasz na zdezorientowanego")
                        delay_print("Pewnie zastanawiasz się o co tu chodzi. Nic dziwnego.")
                        delay_print("Postaram Ci się wszystko wyjąśnić tak abyś jak najlepiej zrozumiał")
                        delay_print("Otóż było to 3 lata temu, zostałeś skazany i umieszczony tutaj")
                        delay_print("Chcesz wiedzieć za co? Pewnego dnia gdy byłeś podłączony do sieci i grałeś w soją ulubioną grę.")
                        delay_print("Brałeś udział w turnieju, po wygraniu którego miałeś zdobyć najwyższą rangę. Nagle jednak połączenie z siecią zostało przerwane ")
                        delay_print("Rozwścieczyło Cię to. Zacząłeś walić pięściami w ściany i krzyczeć.")
                        delay_print("Do pokoju weszła twoja matka i powiedziała że to ona wyłączyła prąd.")
                        delay_print("Miała dość ciebie i tego że ciągle tylko marnujesz czas ")
                        delay_print("Jednak ty byłeś w takim amoku że rzuciłeś się na nią.")
                        delay_print("Poderżnąłeś jej gardło nożem który znajdował się na twoim biurku. Potem sam zgłosiłeś się na policję.")
                        delay_print("Hmmmmmmm? Nie patrz tak na mnie. To TY jesteś mordercą "+name+", a nie ja.")
                        delay_print("Zresztą nie powinieneś narzekać teraz cały czas znajdujesz się w grzę, tak jak chciałeś")
                        delay_print("Wszystko to co się wydarzyło jest tylko symulacją, która powtarza się w kółko.")
                        delay_print("Zmienione są tylko niektóre detale a twoja pamięć jest kasowana. To co masz to tylko fałszywe wspomnienia")
                        delay_print("HaHaHa. Żałuj że nie widzisz teraz swojej miny.")
                        delay_print("Uwielbiam ten moment gdy Ci to wszystko opowiadam naprwdę.")
                        delay_print("Twoja męka i cierpienie są emitowane na specjalnych galach PPV")
                        delay_print("Jesteś naszą małpką cyrkową. Tylko że nikomu nie jest Ciebie szkoda.")
                        delay_print("Nikt Ci nie pomoże ani nie uratuje. Będziesz przeżywał ten sam koszmar dzień w dzień bez końca.")
                        delay_print("O kurde. Już ta godzina? Musimy się spieszyć za 10 minut kolejny pokaz. Za chwilę twoja pamięć zostanie wykasowana.")
                        delay_print("Tym razem daj z siebie wszystko! To mówiąc uśmiechnął się, odwrócił plecami i odszedł.")
                        q=input("Wpisz cokolwiek aby wyjść: ")
                        quit()

                    else:
                        print("wybierz dostępną opcję")









else:
    print("A więc żegnaj")
    quit()

