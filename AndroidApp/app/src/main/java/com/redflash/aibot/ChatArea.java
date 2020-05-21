package com.redflash.aibot;

import android.content.Context;
import android.graphics.Color;
import android.graphics.Typeface;
import android.view.Gravity;
import android.view.View;
import android.view.ViewGroup;
import android.widget.EditText;
import android.widget.LinearLayout;
import android.widget.ScrollView;
import android.widget.TextView;

import java.util.StringTokenizer;

import static com.redflash.aibot.MainActivity.BOT;
import static com.redflash.aibot.MainActivity.USER;
import static com.redflash.aibot.MainActivity.INFO;

public class ChatArea {

    private CloudLink link;
    private EditText etChatbar;
    private LinearLayout llChat;
    private ScrollView svChat;
    private Context context;

    ChatArea(CloudLink link, EditText etChatbar, LinearLayout llChat, ScrollView svChat, Context context) {
        this.link = link;
        this.etChatbar = etChatbar;
        this.llChat = llChat;
        this.svChat = svChat;
        this.context = context;
    }

    public void processInput(View v, String input) {
        if (isCommand(input)) {
            String command = input.substring(1);
            runCommand(v, command);
            return;
        }

        createBubble(v, input, USER);
        TextView temp = createBubble(v, getString(R.string.loading), BOT);
        link.reply(input, temp);
    }

    private boolean isCommand(String input) {
        return (input.charAt(0) == '/');
    }

    private void runCommand(View v, String command) {
        StringTokenizer st = new StringTokenizer(command);
        if (st.countTokens() < 1) return;
        switch (st.nextToken()) {
            case "server": {
                if(st.hasMoreTokens()) {
                    String url = st.nextToken();
                    link.setUrl(url);
                    createBubble(v, "Server URL changed successfully to: "+url, INFO);
                    return;
                }
                break;
            }
            default: {
                break;
            }
        }

        createBubble(v, "Invalid Command", INFO);
    }

    private TextView createBubble(View v, String text, int sender) {

        TextView temp = new TextView(v.getContext());
        temp.setText(text);
        temp.setLayoutParams(new ViewGroup.LayoutParams(
                ViewGroup.LayoutParams.WRAP_CONTENT,
                ViewGroup.LayoutParams.WRAP_CONTENT));
        temp.setTextSize(2, 20);
        temp.setPadding(10, 4, 10, 4);


        if (sender == USER) {
            temp.setBackgroundResource(R.drawable.chatshape);
            temp.setTextColor(Color.BLUE);
            temp.setTextAlignment(View.TEXT_ALIGNMENT_TEXT_END);
            LinearLayout.LayoutParams params = new LinearLayout.LayoutParams(LinearLayout.LayoutParams.WRAP_CONTENT, LinearLayout.LayoutParams.WRAP_CONTENT);
            params.gravity = Gravity.END; //despite the confusing name, this is on Layout params and this is layout_gravity
            params.weight = 1.0f;
            temp.setLayoutParams(params);
        }
        else if (sender == INFO) {
            temp.setBackgroundResource(R.drawable.infoshape);
            temp.setTextColor(Color.GRAY);
            temp.setTextAlignment(View.TEXT_ALIGNMENT_TEXT_END);
            temp.setTypeface(null, Typeface.ITALIC);
            LinearLayout.LayoutParams params = new LinearLayout.LayoutParams(LinearLayout.LayoutParams.WRAP_CONTENT, LinearLayout.LayoutParams.WRAP_CONTENT);
            params.gravity = Gravity.CENTER; //despite the confusing name, this is on Layout params and this is layout_gravity
            params.weight = 1.0f;
            temp.setLayoutParams(params);
        }
        else { // if (sender == BOT)
//            temp.setBackgroundResource(R.color.gray);
            temp.setBackgroundResource(R.drawable.chatshape);
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

    private String getString(int n) {
        return context.getString(n);
    }

}
