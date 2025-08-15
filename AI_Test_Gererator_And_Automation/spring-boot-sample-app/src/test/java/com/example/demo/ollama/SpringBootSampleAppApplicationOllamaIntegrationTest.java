package com.example.demo.ollama;

import com.example.demo.SpringBootSampleAppApplication;
import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.web.servlet.MockMvc;
import org.springframework.test.web.servlet.setup.MockMvcBuilders;

@SpringBootTest(classes = SpringBootSampleAppApplication.class)
public class SpringBootSampleAppApplicationOllamaIntegrationTest {

	private MockMvc mockMvc;

	@Test
	void contextLoads() throws Exception {
		mockMvc = MockMvcBuilders.standaloneSetup(new SpringBootSampleAppApplication()).build();
	}

}