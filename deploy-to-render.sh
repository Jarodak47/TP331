#!/bin/bash

# Backend
curl -X POST -H "Authorization: Bearer $RENDER_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{"serviceId": "<backend-service-id>", "clearCache": false}' \
    "https://api.render.com/v1/services/<backend-service-id>/deploys"
