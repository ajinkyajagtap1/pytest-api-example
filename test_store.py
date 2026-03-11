import pytest
import requests

BASE_URL = "http://127.0.0.1:5000"

def test_patch_order_status():
    # 1. Place an order for pet ID 2 (flippy)
    order_payload = {"pet_id": 2}
    post_res = requests.post(f"{BASE_URL}/store/order", json=order_payload)
    order_id = post_res.json()["id"]

    # 2. PATCH the status to 'sold'
    patch_payload = {"status": "sold"}
    response = requests.patch(f"{BASE_URL}/store/order/{order_id}", json=patch_payload)
    
    assert response.status_code == 200
    assert response.json()["message"] == "Order and pet status updated successfully"

    # 3. Verify pet status changed to 'sold'
    pet_res = requests.get(f"{BASE_URL}/pets/2")
    assert pet_res.json()["status"] == "sold"