PANEL BLOGA — PAGES CMS + GITHUB + NETLIFY

CO JEST GOTOWE
- Plik .pages.yml konfiguruje panel do pisania artykułów.
- Artykuły są w katalogu _posts/ w formacie Markdown.
- Nowy artykuł dostaje automatycznie własny adres /blog/nazwa-pliku/.
- Skrypt python scripts/build.py automatycznie aktualizuje listę artykułów, podstrony i sitemap.xml.
- Pole draft=true ukrywa artykuł przed publikacją.
- SEO: title, description, canonical, Open Graph i BlogPosting dla każdego artykułu.

JAK URUCHOMIĆ PANEL (jednorazowo)
1. Załóż konto na github.com i utwórz PRYWATNE repozytorium.
2. Wgraj do repozytorium CAŁĄ zawartość tego folderu (również ukryty plik .pages.yml).
   UWAGA: GitHub web upload może pomijać ukryte pliki — upewnij się, że .pages.yml istnieje w repozytorium.
3. Na app.netlify.com wybierz Add new project → Import an existing project → GitHub.
   Połącz to samo repozytorium. Netlify odczyta netlify.toml:
   build: python -m pip install PyYAML mistune && python scripts/build.py, publish: dist.
4. Wejdź na https://pagescms.org/ i zaloguj się kontem GitHub. Autoryzuj dostęp
   do tego repozytorium zgodnie z instrukcjami Pages CMS.
5. Wybierz repozytorium → Artykuły bloga → New. Wpisz tytuł, opis SEO,
   kategorię, datę i treść. Ustaw draft=false, gdy chcesz opublikować.
6. Zapisz. Pages CMS zapisze plik w GitHub; Netlify automatycznie przebuduje stronę.
   Publikacja wymaga prawidłowo działającej integracji GitHub-Netlify.

WAŻNE
- Ten ZIP sam w sobie NIE zapewnia działającego logowania do panelu.
- Samo przesłanie ZIP/folderu przez Netlify Drop NIE uruchamia automatycznych aktualizacji CMS.
- Konieczne jest podłączenie repozytorium GitHub i wdrożenia Netlify.
- Pierwsze trzy artykuły zostały przeniesione do _posts/ i pozostają edytowalne.
- Nie udostępniaj publicznie dostępu do repozytorium; do panelu loguj się przez GitHub.
- Weryfikuj merytorycznie i prawnie publikowane treści psychologiczne.
