package com.redflash.aibot;

import androidx.appcompat.app.AppCompatActivity;

import android.graphics.Color;
import android.graphics.Typeface;
import android.os.Bundle;
import android.view.Gravity;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.EditText;
import android.widget.LinearLayout;
import android.widget.ScrollView;
import android.widget.TextView;

import java.util.StringTokenizer;

public class MainActivity extends AppCompatActivity {

    static final int USER = 1;
    static final int BOT = 0;

    CloudLink link;

    EditText etChatbar;
    Button btnSend;
    LinearLayout llChat;
    ScrollView svChat;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        link = new CloudLink(getString(R.string.bot_server), this);

        etChatbar = findViewById(R.id.etChatbar);
        btnSend = findViewById(R.id.btnSend);
        llChat = findViewById(R.id.llChat);
        svChat = findViewById(R.id.svChat);

        btnSend.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                String input = etChatbar.getText().toString();
                if(input.equals(""))
                    return;
                else if (isCommand(input)) {
                    String command = input.substring(1);
                    runCommand(v, command);
                }

                createBubble(v, input, USER);
                TextView temp = createBubble(v, getString(R.string.loading), BOT);
                link.reply(input, temp);
            }
        });

    }

    private void runCommand(View v, String command) {
        StringTokenizer st = new StringTokenizer(command);
        if (st.countTokens() < 1) return;
        switch (st.nextToken()) {
            case "server": {
                if(st.hasMoreTokens()) {
                    link.setUrl(st.nextToken());
                    createBubble(v, "Server URL changed successfully", BOT);
                    return;
                }
                break;
            }
            default: {
                break;
            }
        }

        createBubble(v, "Invalid Command", BOT);
    }

    private boolean isCommand(String input) {
        return (input.charAt(0) == '/');
    }

    private TextView createBubble(View v, String text, int sender) {

        TextView temp = new TextView(v.getContext());
        temp.setText(text);
        temp.setLayoutParams(new ViewGroup.LayoutParams(
                ViewGroup.LayoutParams.WRAP_CONTENT,
                ViewGroup.LayoutParams.WRAP_CONTENT));
        temp.setTextSize(2, 20);
        temp.setPadding(10, 4, 10, 4);
        temp.setBackgroundResource(R.drawable.chatshape);


        if (sender == USER) {
//            temp.setBackgroundResource(R.color.white);
            temp.setTextColor(Color.BLUE);
            temp.setTextAlignment(View.TEXT_ALIGNMENT_TEXT_END);
            LinearLayout.LayoutParams params = new LinearLayout.LayoutParams(LinearLayout.LayoutParams.WRAP_CONTENT, LinearLayout.LayoutParams.WRAP_CONTENT);
            params.gravity = Gravity.END; //despite the confusing name, this is on Layout params and this is layout_gravity
            params.weight = 1.0f;
            temp.setLayoutParams(params);
        }
        else { // if (sender == BOT)
//            temp.setBackgroundResource(R.color.gray);
            if(text.equals(getString(R.string.loading))) {
                temp.setTextColor(Color.GRAY);
            }
            else { // this is again set in CloudLink.java when successful response is received
                temp.setTypeface(null, Typeface.ITALIC);
                temp.setTextColor(Color.DKGRAY);
            }
        }

        etChatbar.setText("");
        llChat.addView(temp);
        svChat.fullScroll(View.FOCUS_DOWN);
        final ViewGroup.MarginLayoutParams lpt = (ViewGroup.MarginLayoutParams) temp.getLayoutParams();
        int left, right;
        if(sender == USER) {
            left = 150;
            right = 10;
        }
        else {
            left = 10;
            right = 150;
        }
        lpt.setMargins(left,8,right,8);

        return temp;
    }
}
