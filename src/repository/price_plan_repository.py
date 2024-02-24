class PricePlanRepository:
    def __init__(self) -> None:
        self.price_plans = []
        pass

    def store(self, new_price_plans):
        self.price_plans += new_price_plans

    def get(self):
        return self.price_plans.copy()
    
    def clear(self):
        self.price_plans=[]

price_plan_repository = PricePlanRepository()