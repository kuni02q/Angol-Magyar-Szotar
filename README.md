# Magyar-Angol Szótár 

Ez egy egyszerű Django alapú webes alkalmazás, amely lehetővé teszi magyar-angol szópárok hozzáadását, megtekintését és gyakorlását. Az alkalmazás célja, hogy segítse a felhasználókat a nyelvtanulásban és a szókincs fejlesztésében.

## Funkciók

- **Szópárok hozzáadása**
- **Szótár megtekintése**
- **Gyakorlás**

## Használat
- Szópár hozzáadása: Új szópárokat adhatsz hozzá a szótárhoz.
- Szótár megtekintése: Megtekintheted a szótárban lévő összes szópárt.
- Gyakorlás indítása: Gyakorolhatod a szavakat véletlenszerű kérdésekkel.


![Screenshot_7](https://github.com/user-attachments/assets/1c0ffde1-6700-4cdf-83fe-56be19ab20da)


![Screenshot_8](https://github.com/user-attachments/assets/f3d3046d-e0fe-4545-b3a3-6da363060a44)


![Screenshot_9](https://github.com/user-attachments/assets/e4b68d00-5822-4d69-b70e-be76caf5fff9)




Funkcionális Specifikáció
1. Áttekintés
A Magyar-Angol Szótár egy olyan webes alkalmazás, amely lehetővé teszi a felhasználók számára, hogy magyar és angol szópárokat tanuljanak, gyakoroljanak, valamint új szópárokat adjanak hozzá a szótárhoz. Az alkalmazás célja, hogy a felhasználók hatékonyan fejleszthessék szókincsüket, és játékos formában teszteljék tudásukat. Az alkalmazás bármely internetes böngészőből elérhető, és egyszerű, felhasználóbarát felülettel rendelkezik, hogy mindenki számára könnyen használható legyen. Az alkalmazás célcsoportja diákok, nyelvtanulók és bárki, aki szeretné bővíteni a magyar-angol szókincsét.

2. Jelenlegi helyzet
Jelenleg nincs könnyen hozzáférhető eszköz, amely lehetővé tenné a felhasználóknak, hogy egyszerűen és gyorsan hozzáférjenek magyar-angol szópárokhoz, és gyakorolják azokat. A hagyományos szótárak és nyelvtanuló applikációk korlátozott funkciókat nyújtanak, és gyakran nem tartalmaznak lehetőséget arra, hogy a felhasználók saját szópárokat adjanak hozzá, vagy saját tempójukban gyakoroljanak. Ezért szükség van egy olyan modern webes alkalmazásra, amely játékos formában támogatja a szótanulást, és lehetővé teszi a felhasználóknak, hogy bármikor, bárhonnan elérhessék és gyakorolják a szavakat.

3. Követelménylista
Az alábbiakban található a rendszer funkcióinak listája:

## Követelménylista

| Modul ID | Név                  | Kifejtés                                                                                                                                           |
|----------|----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| K1       | Szópár hozzáadása    | A felhasználó új magyar-angol szópárokat adhat hozzá a szótárhoz. A felhasználó megadhat egy magyar szót/mondatot és annak angol megfelelőjét.      |
| K2       | Szótár megtekintése  | A felhasználó megtekintheti az összes szópárt, amelyet korábban hozzáadtak az alkalmazáshoz. A szópárok listázása átlátható és kereshető.           |
| K3       | Gyakorlás indítása   | A felhasználó véletlenszerűen kiválasztott szópárokkal gyakorolhat, és megpróbálhatja helyesen lefordítani azokat. A gyakorlás végén a rendszer értékeli a teljesítményt. |
| K4       | Eredmények megtekintése | A felhasználó megtekintheti, hogy a gyakorlás során hány helyes választ adott, és hol hibázott. Az eredmények segítik a felhasználó fejlődésének nyomon követését. |
| K5       | Admin felület        | Az adminisztrátorok új szópárokat adhatnak hozzá, módosíthatják vagy törölhetik a meglévőket, valamint felügyelhetik a felhasználók által hozzáadott tartalmakat. |


4. Jelenlegi üzleti folyamatok modellje
A hagyományos szótárak és nyelvtanulási platformok korlátozott lehetőségeket nyújtanak. A felhasználók csak előre meghatározott szópárokat tanulhatnak, és gyakran nem kapnak lehetőséget saját tartalom hozzáadására. Ez a korlátozás nehezíti a tanulási folyamat személyre szabását, és sok felhasználó nem találja érdekesnek vagy hasznosnak a statikus szótárakat. Az oktatási intézmények és a nyelvtanulók számára szükség van egy rugalmasabb, játékosabb megközelítésre.

5. Igényelt üzleti folyamatok modellje
A Magyar-Angol Szótár alkalmazás célja, hogy modern és interaktív megoldást nyújtson a szótanulásra. A felhasználók saját szópárokat adhatnak hozzá, amelyeket később gyakorolhatnak. A gyakorlási funkció azonnali visszajelzést biztosít a felhasználóknak, így nem kell hosszasan várniuk az eredményekre. Az adminisztrátorok felügyelhetik a szótár tartalmát, biztosítva ezzel, hogy a hozzáadott szópárok helyesek és relevánsak legyenek.

6. Használati esetek
Felhasználó: A felhasználó bejelentkezés nélkül is megtekintheti a nyilvános szópárokat, és elkezdheti a gyakorlást. Bejelentkezés után lehetősége van új szópárokat hozzáadni, és megtekintheti a saját eredményeit.
Adminisztrátor: Az adminisztrátor hozzáfér a teljes szótárhoz, új szópárokat adhat hozzá, szerkesztheti vagy törölheti a meglévő tartalmat, valamint ellenőrizheti a felhasználók által hozzáadott szópárokat.
7. Megfeleltetés, hogyan fedik le a használati esetek a követelményeket
Szópár hozzáadása (K1) - Felhasználói hozzáférés
Szótár megtekintése (K2) - Nyilvános hozzáférés
Gyakorlás indítása (K3) - Felhasználói hozzáférés
Eredmények megtekintése (K4) - Felhasználói hozzáférés
Admin felület (K5) - Adminisztrátori hozzáférés
8. Képernyő tervek
A Magyar-Angol Szótár alkalmazás felépítése egyszerű és felhasználóbarát. A főoldalon a felhasználók választhatnak a következő lehetőségek közül: "Szópár hozzáadása", "Szótár megtekintése" és "Gyakorlás indítása". A felületen van egy nyelvváltó kapcsoló is, amely lehetővé teszi a magyar és angol nyelv közötti váltást.

9. Forgatókönyv
Forgatókönyv: Szópár hozzáadása
A felhasználó bejelentkezik az alkalmazásba.
A felhasználó a "Szópár hozzáadása" opcióra kattint.
Megjelenik egy űrlap, ahol a felhasználó beírhat egy magyar szót és annak angol megfelelőjét.
A felhasználó elküldi az űrlapot.
A rendszer ellenőrzi az adatokat, és sikeres hozzáadás esetén tárolja az adatbázisban.
A felhasználó egy visszajelzést kap arról, hogy a szópárt sikeresen hozzáadták.
10. Funkció - követelmény megfeleltetés
Szópár hozzáadása (K1) - Felhasználói igény, saját szópárok hozzáadása.
Szótár megtekintése (K2) - Felhasználói igény, meglévő szavak böngészése.
Gyakorlás indítása (K3) - Felhasználói igény, tudás ellenőrzése.
Admin felület (K5) - Adminisztrátori felügyelet és tartalomkezelés.
11. Fogalomszótár
Adminisztrátor: A rendszer felügyeletéért és karbantartásáért felelős személy.
Felhasználó: A rendszerben bejelentkezett személy, aki szópárokat adhat hozzá és gyakorolhatja azokat.
Nyelvváltó: Egy kapcsoló, amellyel a felhasználó válthat a magyar és az angol felület között.
Szópár: Magyar és angol nyelven megadott szavak vagy kifejezések, amelyek egymás fordításai.
