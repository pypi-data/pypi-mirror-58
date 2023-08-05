{{#general_title}}
# {{{title}}}

{{/general_title}}

{{#versions}}
{{#solicited_requests}}### {{{solicited_requests}}}{{/solicited_requests}}

{{#sections}}

{{#commits}}

{{#tags}}#{{{tags}}}{{/tags}}

{{#condition_i}}### **[{{{second_parameter}}}]({{{jira_url}}}/{{{second_parameter}}})**{{/condition_i}}{{^condition_i}}{{{second_parameter}}}{{/condition_i}}

**DATE:** {{{date}}}

**TITLE:** {{#condition_i}}{{{third_parameter}}}{{/condition_i}}{{^condition_i}}{{{subject}}}{{/condition_i}}

{{#body}}{{{body_indented}}}{{/body}}

* * *

{{/commits}}
{{/sections}}

{{/versions}}
