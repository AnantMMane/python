org.springframework.cloud.contract.spec.Contract.make {
    request {
        method 'GET'
        url '/hello'
    }
    response {
        status 200
        body([
            message: "Hello from Spring Boot!"
        ])
        headers {
            contentType(applicationJson())
        }
    }
} 