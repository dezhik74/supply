from django.db import models


class Orders(models.Model):
    date = models.DateField(auto_now_add=True, verbose_name='Дата')
    address = models.CharField(max_length=255, verbose_name='Объект')
    responsible = models.CharField(max_length=255, verbose_name='Прораб')
    closed = models.BooleanField(default=False, verbose_name='Исполнен')
    notes = models.CharField(max_length=1000, verbose_name='Примечания')

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"

    def __str__(self):
        return f'Заявка от {self.date} на {self.address}'


class OrderItems(models.Model):
    position = models.IntegerField(verbose_name='N пп')
    name = models.CharField(max_length=500, verbose_name='Наименование')
    unit = models.CharField(max_length=10, verbose_name='е.и.')
    quantity = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Кол-во')
    note = models.CharField(max_length=255, verbose_name='Примечание')
    closed = models.BooleanField(default=False, verbose_name='Исполнен')
    order = models.ForeignKey('Orders', on_delete=models.CASCADE, related_name='orderitem', verbose_name='Заявка')

    class Meta:
        verbose_name = "Строка заявки"
        verbose_name_plural = "Строки заявки"

    def __str__(self):
        return f'Строка -> {self.name}'


class OrderMedia(models.Model):
    file_name = models.FileField(upload_to='order_media/%Y/%m/%d/', blank=True, verbose_name='Файл к заявке')
    order = models.ForeignKey('Orders', on_delete=models.CASCADE, related_name='ordermedia', verbose_name='Заявка')

    class Meta:
        verbose_name = "Картинка к заявке"
        verbose_name_plural = "Картинки к заявке"

    def __str__(self):
        return self.filename


class Invoices(models.Model):
    supplier = models.CharField(max_length=100, verbose_name='Поставщик')
    number = models.CharField(max_length=100, verbose_name='Номер')
    date = models.DateField(auto_now_add=True, verbose_name='Дата')
    sum = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма')
    order = models.ForeignKey('Orders', on_delete=models.CASCADE, related_name='invoice', verbose_name='Счет')

    class Meta:
        verbose_name = "Счет"
        verbose_name_plural = "Счета"

    def __str__(self):
        return f'Счет №{self.number} от {self.date} на сумму {self.sum}'


class Delivers(models.Model):
    deliver_date = models.DateField(auto_now_add=True, verbose_name='Дата доставки')
    transporter = models.CharField(max_length=100, verbose_name='Перевозчик', unique_for_date=deliver_date)

    class Meta:
        verbose_name = "Доставка"
        verbose_name_plural = "Доставки"

    def __str__(self):
        return f'{self.deliver_date} -> {self.transporter}'


class DeliverItems(models.Model):
    invoice = models.ForeignKey(
        'Invoices',
        on_delete=models.CASCADE,
        related_name='delivery',
        verbose_name='Счет',
        blank=True
    )
    deliver_date = models.ForeignKey(
        'Delivers',
        on_delete=models.CASCADE,
        related_name='delivery_item',
        verbose_name='Доставка'
    )
    note = models.CharField(max_length=500, verbose_name='Примечание')

    class Meta:
        verbose_name = "Ходка"
        verbose_name_plural = "Ходки"

    def __str__(self):
        return f'{self.pk}'
