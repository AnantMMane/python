org.springframework.cloud.contract.spec.Contract.make {
    request {
        method 'PUT'
        urlPath('/hello/123')
        body([
            status: "active"
        ])
        headers {
            contentType(applicationJson())
        }
    }
    response {
        status 200
        body([
            message: "PUT received!",
            id: "123",
            updated: [
                status: "active"
            ]
        ])
        headers {
            contentType(applicationJson())
        }
    }
} 