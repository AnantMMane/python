package com.example.demo.ollama;

import com.example.demo.controller.HelloController;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.WebMvcTest;
import org.springframework.http.MediaType;
import org.springframework.test.web.servlet.MockMvc;

import java.util.HashMap;

import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.*;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.content;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

@WebMvcTest(HelloController.class)
public class HelloControllerOllamaUnitTest {

    @Autowired
    private MockMvc mockMvc;

    @Test
    public void testGetHello() throws Exception {
        this.mockMvc.perform(get("/hello"))
                .andExpect(status().isOk())
                .andExpect(content().string("{\"message\":\"Hello from Spring Boot!\"}"))
                .andReturn();
    }

    @Test
    public void testPostHello() throws Exception {
        this.mockMvc.perform(post("/hello")
                        .contentType(MediaType.APPLICATION_JSON)
                        .content("{\"name\":\"John\"}"))
                .andExpect(status().isOk())
                .andExpect(content().json("{\"message\":\"POST received!\",\"received\":{\"name\":\"John\"}}"))
                .andReturn();
    }

    @Test
    public void testPutHello() throws Exception {
        this.mockMvc.perform(put("/hello/1")
                        .contentType(MediaType.APPLICATION_JSON)
                        .content("{\"age\":30}"))
                .andExpect(status().isOk())
                .andExpect(content().json("{\"message\":\"PUT received!\",\"id\":\"1\",\"updated\":{\"age\":30}}"))
                .andReturn();
    }
}