# email_validator

Walidacja adresów email. Sprawdza wiele kryteriów, czy adres ma prawidłową formę, czy domena jest zarejestrowane, itp.
Wymaga biblioteki Pythona pyIsEmail do pobrania tutaj https://pypi.org/project/pyIsEmail/#description
Wystarczy pobrać i zainstalować
``` sudo python3 setup.py install ```

wyjście można przekierować do pliku i zaimportować np. do XLSX, przykład poniżej:
```pedobear2@pthc:~/$ python3 email.py > email.txt
a@3.SM;<DNSDiagnosis: NO_RECORD>
a7g3P@q.mD;<ValidDiagnosis: VALID>
a846115220444c9b7d6a2ef9e1589dc@sentry.io;<ValidDiagnosis: VALID>
a@.aK.aQ.aS;<InvalidDiagnosis: DOT_START>
ABEF65@S.aZ;<DNSDiagnosis: NO_RECORD>
a@BK.tz;<DNSDiagnosis: NO_RECORD>
ABoolVal@ues.No;<ValidDiagnosis: VALID>
ac@acabogacia.org;<ValidDiagnosis: VALID>
accv@accv.es;<ValidDiagnosis: VALID>
acraiz@suscerte.gob.ve;<DNSDiagnosis: NO_NAMESERVERS>
acrse@economia.gob.mx;<ValidDiagnosis: VALID>
activity-stream@mozilla.org;<ValidDiagnosis: VALID>
addonhack@mozilla.kewis.ch;<ValidDiagnosis: VALID>
admin@allani.pl;<ValidDiagnosis: VALID>
admin_ca@mtin.es;<ValidDiagnosis: VALID>
admin@sadistic.pl;<ValidDiagnosis: VALID>
alejandro.martinez-chacin@gameloft.co;<ValidDiagnosis: VALID>
appro@openssl.org;<ValidDiagnosis: VALID>
atibilit@y.Data;<DNSDiagnosis: NO_RECORD>
Az@.AzP.Az;<InvalidDiagnosis: DOT_START>
