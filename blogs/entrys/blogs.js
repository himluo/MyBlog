import pager from 'vue-simple-pager';
import Vue from 'vue';
import moment from 'moment';

var TIMESINCE_CHUNKS = new Map([
    ['year', 60 * 60 * 24 * 365],
    ['month', 60 * 60 * 24 * 30],
    ['week', 60 * 60 * 24 * 7],
    ['day', 60 * 60 * 24],
    ['hour', 60 * 60],
    ['minute', 60],
]);

Vue.filter('moment', function (value, formatString) {
    formatString = formatString || 'YYYY-MM-DD HH:mm:ss';
    return moment(value).format(formatString);
});

Vue.filter('prefix', function(value, prefix) {
    return prefix + value;
});

Vue.filter('suffix', function(value, suffix) {
    return value + suffix;
});

function getBlogPage(page, func) {
    $.getJSON(
        'api/blogs', {
            page: page,
        },
        function(data) {
            func(data);
        }
    )
}

function initVM(results) {
    var vm = new Vue({
        el: '#vm',
        data: {
            count: results.count,
            blogs: results.results,
        },
        computed: {
            totalPage: function() {
                return Math.ceil(this.count / 5);
            },
        },
        methods: {
            goPage: function(data){
                getBlogPage(data.page, (results) => {
                    this.blogs = results.results;
                });
            },
        },

        components: {
            'pager': pager
        },
    });
}

$(function () {
    getBlogPage(1, initVM);
});


