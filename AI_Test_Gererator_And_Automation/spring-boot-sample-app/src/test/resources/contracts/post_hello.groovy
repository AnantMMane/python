org.springframework.cloud.contract.spec.Contract.make {
    request {
        method 'POST'
        url '/hello'
        body([
            name: "Alice",
            age: 30
        ])
        headers {
            contentType(applicationJson())
        }
    }
    response {
        status 200
        body([
            message: "POST received!",
            received: [
                name: "Alice",
                age: 30
            ]
        ])
        headers {
            contentType(applicationJson())
        }
    }
} 