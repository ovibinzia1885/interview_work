from django.db import models


# Create your models here.

class AccountHeads(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class AccountType(models.Model):
    id = models.AutoField(primary_key=True)
    acc_type_name = models.CharField(max_length=50)
    acc_head = models.ForeignKey(AccountHeads, on_delete=models.CASCADE)

    def __str__(self):
        return self.acc_type_name


class AccountName(models.Model):
    id = models.AutoField(primary_key=True)
    acc_name = models.CharField(max_length=50)
    type_of_acc = models.ForeignKey(AccountType, on_delete=models.CASCADE)
    opening_balance = models.FloatField()
    closing_balance = models.FloatField()

    def __str__(self):
        return self.acc_name


class JournalLog(models.Model):
    id = models.AutoField(primary_key=True)
    transaction_date = models.DateTimeField(null=True)
    reference_no = models.CharField(max_length=50)

    def __str__(self):
        return str(self.transaction_date)


class JournalLogDetails(models.Model):
    id = models.AutoField(primary_key=True)
    journal_log = models.ForeignKey(JournalLog, on_delete=models.CASCADE)
    account_name = models.ForeignKey(AccountName, on_delete=models.CASCADE)
    amount = models.FloatField()

    def __str__(self):
        return str(self.journal_log.transaction_date) + self.account_name.acc_name
