from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Utente(models.Model):
    user_auth = models.OneToOneField(User, primary_key=True)

    telefono = models.CharField(max_length=20, verbose_name="Cellulare",
                             null=True, default=None, blank=True)

    dataDiNascita = models.DateField(verbose_name="data di nascita", null=True,
                                 default=None, blank=True)
    def __str__(self):
        return self.user_auth.username

class Tecnico(Utente):

    oreRecupero = models.FloatField(verbose_name='ore da recuperare', null=True, default=None, blank=True);

    lavoroQuota = models.BooleanField(verbose_name='Lavoro in quota', default=True);

    def __str__(self):
        return self.user_auth.last_name

class Amministrativo(Utente):

    pass

class Cliente(models.Model):

    codiceCliente = models.CharField(max_length=500, verbose_name='Codice cliente', null=True, blank=True)

    Intestazione = models.CharField(max_length=500, verbose_name='Intestazione', null=True, blank=True)

    RagioneSociale = models.CharField(max_length=200, verbose_name='Ragione sociale')

    Indirizzo = models.CharField(max_length=500, verbose_name='Indirizzo', null=True, blank=True)

    CAPComune = models.CharField(max_length=500, verbose_name='Cap e Comune', null=True, blank=True)

    Comune = models.CharField(max_length=500, verbose_name='Comune', null=True, blank=True)

    RSComune = models.CharField(max_length=500, verbose_name='Ragione Sociale e Comune', null=True, blank=True)

    indirizzoFat = models.CharField(max_length=500, verbose_name='Indirizzo fatturazione', null=True, blank=True)

    CAPFat = models.CharField(max_length=500, verbose_name='CAP fatturazione', null=True, blank=True)

    comuneFat = models.CharField(max_length=500, verbose_name='Comune fatturazione', null=True, blank=True)

    PartitaIva = models.CharField(max_length=500, verbose_name='Partita Iva', null=True, blank=True)

    codiceFiscale = models.CharField(max_length=500, verbose_name='Codice Fiscale', null=True, blank=True)

    condizioniPagamento = models.CharField(max_length=500, verbose_name='Condizioni di pagamento', null=True, blank=True)

    Telefono = models.CharField(max_length=500, verbose_name='Telefono', null=True, blank=True)

    Fax = models.CharField(max_length=500, verbose_name='FAX', null=True, blank=True)

    Email = models.CharField(max_length=500, verbose_name='Email', null=True, blank=True)

    note = models.TextField(max_length=500, verbose_name='Note', null=True, blank=True)

    titolo2 = models.CharField(max_length=500, verbose_name='Titolo', null=True, blank=True)

    Referente2 = models.CharField(max_length=500, verbose_name='Referente', null=True, blank=True)

    cognome2 = models.CharField(max_length=500, verbose_name='Cognome', null=True, blank=True)

    Telefono2 = models.CharField(max_length=500, verbose_name='Telefono', null=True, blank=True)

    Fax2 = models.CharField(max_length=500, verbose_name='Fax', null=True, blank=True)

    Email2 = models.CharField(max_length=500, verbose_name='Email', null=True, blank=True)

    titolo3 = models.CharField(max_length=500, verbose_name='Titolo', null=True, blank=True)

    Referente3 = models.CharField(max_length=500, verbose_name='Referente', null=True, blank=True)

    cognome3 = models.CharField(max_length=500, verbose_name='Cognome', null=True, blank=True)

    Telefono3 = models.CharField(max_length=500, verbose_name='Telefono1', null=True, blank=True)

    Fax3 = models.CharField(max_length=500, verbose_name='Fax1', null=True, blank=True)

    Email3 = models.CharField(max_length=500, verbose_name='Email1', null=True, blank=True)


    def __str__(self):
        return self.RagioneSociale

class Giorno(models.Model):
    giorno = models.DateField(null=False, verbose_name='Giorno')

    personaleAssente = models.ManyToManyField(Tecnico, verbose_name='Presonale assente',
                                              related_name='assenze', blank=True)

    def __str__(self):
        ToString = "{}"  # 2 {} placeholders
        return (ToString.format(self.giorno))

class Task(models.Model):

    descrizione = models.CharField(max_length=2000, verbose_name='descrizione')

    oraArrivo = models.CharField(max_length=500, verbose_name='Ora di arrivo')

    cliente = models.ForeignKey(Cliente, verbose_name="Cliente", null=True,
                                default=None, blank=True)

    tecnici = models.ManyToManyField(Tecnico, verbose_name='Tecnici', related_name='taskAssegnati')

    riferimentoCommessa = models.ForeignKey(Amministrativo, verbose_name='Riferimento commessa',
                                            null = True,  default=None)

    note = models.TextField(verbose_name='Note')

    offerta = models.FileField(upload_to='offerte', verbose_name = 'Offerta', null = True)

    giorno = models.ManyToManyField(Giorno, verbose_name='Data', related_name='attivita', default=None)


    def __str__(self):
        ToString = "{} - {}"  # 2 {} placeholders
        return(ToString.format(self.descrizione, self.cliente))










