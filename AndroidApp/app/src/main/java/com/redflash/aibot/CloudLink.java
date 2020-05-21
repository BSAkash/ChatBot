package com.redflash.aibot;

import android.content.Context;
import android.graphics.Color;
import android.graphics.Typeface;
import android.widget.TextView;
import android.widget.Toast;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonObjectRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONObject;

public class CloudLink {

    private Context context;
    private String url;

    CloudLink(String serverUrl, Context context) {
        this.url = serverUrl;
        this.context = context;
    }

//    public boolean serverUp() {
//        return true;
//    }

    public void setUrl(String url) {
        this.url = url;
    }

    public void reply(final String query, final TextView target) {
        // Instantiate the RequestQueue.
        RequestQueue queue = Volley.newRequestQueue(context);

        JSONObject obj = new JSONObject();
        try {
            obj.put("query", query);
        } catch (Exception e) {
            e.printStackTrace();
            Toast.makeText(context, "Error in JSON creation", Toast.LENGTH_SHORT).show();
        }

        // Request a string response from the provided URL.
        JsonObjectRequest stringRequest = new JsonObjectRequest(Request.Method.POST, url, obj,
                new Response.Listener<JSONObject>() {
                    @Override
                    public void onResponse(JSONObject response) {
                        // Display the first 500 characters of the response string.
                        String ans = "Error: no response found in JSON object";
                        target.setTextColor(Color.DKGRAY);
                        target.setTypeface(null, Typeface.NORMAL);
                        try {
                            ans = response.getString("response");
                        } catch (Exception e) {
                            e.printStackTrace();
                            target.setTextColor(Color.RED);
                            target.setTypeface(null, Typeface.BOLD_ITALIC);
                        }
                        target.setText(ans);
//                        Toast.makeText(context, "Success: ", Toast.LENGTH_SHORT).show();
                    }
                },
                new Response.ErrorListener() {
                    @Override
                    public void onErrorResponse(VolleyError error) {
                        target.setText("Network error!");
                        Toast.makeText(context, "Fail: "+error, Toast.LENGTH_LONG).show();
                        error.printStackTrace();
                    }
                }
        );
//        { // our JSON request parameters (POST)
//            @Override
//            protected Map<String, String> getParams() {
//                Map<String, String>  params = new HashMap<>();
//                params.put("query", query);
//                return params;
//            }
//        };
        // Add the request to the RequestQueue.
        queue.add(stringRequest);
    }

}
