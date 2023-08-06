{{#general_title}}
# {{{title}}}

{{/general_title}}

{{#versions}}
{{#solicited_requests}}### {{{solicited_requests}}}{{/solicited_requests}}

{{#sections}}

{{#commits}}

{{#tags}}#{{{tags}}}{{/tags}}

{{#links_or_not}}### **[{{{second_parameter}}}]({{{jira_url}}}/{{{second_parameter}}})**{{/links_or_not}}{{^links_or_not}}{{{second_parameter}}}{{/links_or_not}}

**DATE:** {{{date}}}

**TITLE:** {{#links_or_not}}{{{commit_title}}}{{/links_or_not}}{{^links_or_not}}{{{subject}}}{{/links_or_not}}

{{#body}}{{{body_indented}}}{{/body}}

* * *

{{/commits}}
{{/sections}}

{{/versions}}
