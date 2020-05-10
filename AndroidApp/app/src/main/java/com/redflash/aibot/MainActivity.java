package com.redflash.aibot;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.LinearLayout;
import android.widget.ScrollView;

public class MainActivity extends AppCompatActivity {

    static final int BOT = 0;
    static final int USER = 1;
    static final int INFO = 2;

    CloudLink link;
    ChatArea chat;

    EditText etChatbar;
    Button btnSend;
    LinearLayout llChat;
    ScrollView svChat;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        etChatbar = findViewById(R.id.etChatbar);
        btnSend = findViewById(R.id.btnSend);
        llChat = findViewById(R.id.llChat);
        svChat = findViewById(R.id.svChat);

        link = new CloudLink(getString(R.string.bot_server), this);
        chat = new ChatArea(link, etChatbar, llChat, svChat, this);

        btnSend.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                String input = etChatbar.getText().toString();
                if(input.equals(""))
                    return;
                chat.processInput(v, input);
            }
        });

    }

}
