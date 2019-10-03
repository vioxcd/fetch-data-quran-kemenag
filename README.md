# fetch-data-quran-kemenag
Fetch data Al-Quran dari website kemenag di https://quran.kemenag.go.id/

This project uses [Splash](https://splash.readthedocs.io) to serve as javascript renderer for the Qur'an data.
The surah data is collected using API calls (somehow the Kemenag's API is public) with a 3 second sleep time so that the server isn't flooded with API calls.
