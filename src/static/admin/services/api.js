/**
 * Created by plusplus7 on 2016/10/26.
 */
app.factory('api', function($http, $httpParamSerializer) {
    var apiService = {
        invoke  : function(url, params) {
            var promise = $http({
                url     : url,
                method  : "POST",
                data    : $httpParamSerializer(params),
                headers : {'Content-Type': 'application/x-www-form-urlencoded'}
            }).then(function onSuccess(response) {
                    console.debug(response);
                    return response.data;
                }, function onFail(response) {
                    console.debug(response);
                    var data     = {
                        success : false,
                        msg     : response,
                        data    : "Internal Error"
                    };
                    return data;
                }
            );
            return promise;
        },
        sign : function(params) {
            return "";
        },
        CreateArticle : function(articleId, preview, content) {
            var params = {
                "Action"        : "CreateArticle",
                "Timestamp"      : new Date().getTime(),
                "Key"           : "test",
                "Version"       : "1.0",
                "Signature"     : "",
                "ArticleId"     : articleId,
                "Preview"       : preview,
                "Content"       : content
            };
            params["Signature"] = this.sign(params);
            return this.invoke('/api/CreateArticle', params);
        },
        CreateCategory : function(categoryId, displayName, sectionId, type) {
            var params = {
                "Action"        : "CreateCategory",
                "Timetamp"      : new Date().getTime(),
                "Key"           : "test",
                "Version"       : "1.0",
                "CategoryId"    : categoryId,
                "DisplayName"   : displayName,
                "SectionId"     : sectionId,
                "Type"          : type
            };
            params["Signature"] = this.sign(params);
            return this.invoke('/api/CreateCategory', params);
        },
        ListCategories : function() {
            var params = {
                "Action": "ListCategories",
                "Timestamp": new Date().getTime(),
                "Key": "test",
                "Version": "1.0"
            };
            params["Signature"] = this.sign(params);
            return this.invoke('/api/ListCategories', params);
        },
        AttachArticleToCategory : function(articleId, categoryId) {
            var params = {
                "Action"        : "AttachArticleToCategory",
                "Timestamp"      : new Date().getTime(),
                "Key"           : "test",
                "Version"       : "1.0",
                "ArticleId"     : articleId,
                "CategoryId"    : categoryId
            };
            params["Signature"] = this.sign(params);
            return this.invoke('/api/AttachArticleToCategory', params);
        }
    };
    return apiService;
});
