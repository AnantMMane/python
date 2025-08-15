package com.example.demo.ollama;

import com.example.demo.SpringBootSampleAppApplication;
import org.junit.jupiter.api.Test;
import org.mockito.InjectMocks;
import org.springframework.boot.test.context.SpringBootTest;

import static org.assertj.core.api.AssertionsForClassTypes.assertThat;

@SpringBootTest
class SpringBootSampleAppApplicationOllamaUnitTest {

    @InjectMocks
    private SpringBootSampleAppApplication application;

    @Test
    void contextLoads() {
        assertThat(application).isNotNull();
    }
}