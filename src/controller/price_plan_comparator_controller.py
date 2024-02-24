from flask import abort

from service.account_service import AccountService
from service.price_plan_service import PricePlanService

from controller.electricity_readings_controller import repository 

def compare(smart_meter_id):
    price_plan_service = PricePlanService(repository)
    account_service = AccountService()
    list_of_spend_against_price_plans = price_plan_service.get_list_of_spend_against_each_price_plan_for()

    if len(list_of_spend_against_price_plans)<1:
        abort(404)
    else:
        context = {
            'PricePlanId': account_service.get_price_plan(smart_meter_id=smart_meter_id),
            'PricePlanComparison': list_of_spend_against_price_plans
        }
        return context
    
def recommend(smart_meter_id, limit=None):
    price_plan_service = PricePlanService(repository)
    list_of_spend_against_price_plans = price_plan_service.get_list_of_spend_against_each_price_plan_for(smart_meter_id=smart_meter_id, limit=limit)
    return list_of_spend_against_price_plans.reverse()
