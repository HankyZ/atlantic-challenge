from rest_framework import serializers

from recordManager.models import Customer, Gift, Subscription, Record


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['id', 'plan_name', 'price']


class GiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gift
        fields = ['id', 'plan_name', 'price', 'recipient_email']


class CustomerSerializer(serializers.ModelSerializer):
    subscription = SubscriptionSerializer(required=False)
    gifts = GiftSerializer(many=True)

    class Meta:
        model = Customer
        fields = [
            'id', 'first_name', 'last_name', 'address_1', 'address_2', 'city', 'state', 'postal_code', 'subscription',
            'gifts']


class RecordSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(required=True)

    class Meta:
        model = Record
        fields = ['customer']

    def create(self, validated_data):
        customer_data = validated_data.pop('customer')

        subscription_data = customer_data.pop('subscription')
        gifts_data = customer_data.pop('gifts')

        customer, created = Customer.objects.update_or_create(**customer_data)

        Subscription.objects.update_or_create(customer=customer, **subscription_data)

        for gift_data in gifts_data:
            Gift.objects.update_or_create(customer=customer, **gift_data)

        record, created = Record.objects.update_or_create(customer=customer, **validated_data)

        return record
