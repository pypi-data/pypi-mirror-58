from django.contrib import admin

from meraxes.finance import models


class TransactionAdmin(admin.ModelAdmin):
    def debit(self):
        return '' if self.amount > 0 else f'{self.amount:.2f}'

    def credit(self):
        return f'{self.amount:.2f}' if self.amount > 0 else ''

    list_display = 'date', 'account', debit, credit, 'purpose'
    search_fields = 'purpose',


admin.site.register(models.Account)
admin.site.register(models.Institute)
admin.site.register(models.Transaction, TransactionAdmin)
