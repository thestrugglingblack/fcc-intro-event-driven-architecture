import json

from fastapi import HTTPException


def create_delivery(state, event):
    data = json.loads(event.data)
    return {
        "id": event.delivery_id,
        "budget": int(data["budget"]),
        "notes": data["notes"],
        "status": "ready"
    }


def start_delivery(state, event):
    if state['status'] != 'ready':
        raise HTTPException(status_code=400, detail="Delivery already started")

    state['status'] = 'active'
    return state


def pickup_products(state, event):
    data = json.loads(event.data)
    new_budget = state["budget"] - int(data['purchase_price']) * int(data["quantity"])

    if new_budget < 0:
        raise HTTPException(status_code=400, detail="Not enough budget")

    state['budget'] = new_budget
    state["purchase_price"] = int(data['purchase_price'])
    state["quantity"] = int(data['quantity'])
    state['status'] = 'collected'

    return state


def deliver_products(state, event):
    data = json.loads(event.data)

    new_budget = state["budget"] + int(data['selling_price']) * int(data["quantity"])
    new_quantity = state["quantity"] - int(data['quantity'])

    if new_quantity < 0:
        raise HTTPException(status_code=400, detail="Not enough quantity")

    state['budget'] = new_budget
    state["selling_price"] = int(data['selling_price'])
    state["quantity"] = new_quantity
    state['status'] = 'completed'

    return state


def increase_budget(state, event):
    data = json.loads(event.data)
    state['budget'] += int(data['budget'])
    return state


CONSUMERS = {
    'CREATE_DELIVERY': create_delivery,
    'START_DELIVERY': start_delivery,
    'PICKUP_PRODUCTS': pickup_products,
    'DELIVER_PRODUCTS': deliver_products,
    'INCREASE_BUDGET': increase_budget
}
