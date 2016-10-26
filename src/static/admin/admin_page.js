/**
 * Created by plusplus7 on 2016/10/26.
 */
app.controller('AdminCtrl',
    function($scope, $document, $http, api) {
        api.ListCategories().then(function success(response){
            if (response.Code == 200) {
                $scope.categories = JSON.parse(response.Message);
            } else {
                alert("Load categories Failed! " + response)
            }
        });

        $scope.activeModule = 'AddPost';
        $scope.modules = {
            "AddPost": "active",
            "AddCategory": "",
            "ManagePost": "",
            "ManageCategory": "",
            "ManageAccount": ""
        };
        $scope.moduleOnclick = function(module) {
            $scope.modules[$scope.activeModule] = "";
            $scope.activeModule = module;
            $scope.modules[$scope.activeModule] = "active";
        };

        $scope.editMode = 'Light';
        $scope.editModes = {
            "Light": "active",
            "Raw": ""
        };
        $scope.articleId = "";
        $scope.lightShow = true;
        $scope.editModeOnclick = function(mode) {
            $scope.editModes[$scope.editMode] = "";
            $scope.editMode = mode;
            $scope.editModes[$scope.editMode] = "active";
            $scope.lightShow = mode == "Light";
            $scope.rawShow = mode == "Raw";
        };

        $scope.previewNotShow = true;
        $scope.previewPreviewShow = false;
        $scope.previewPostShow = false;

        $scope.previewPreviewOnClick = function() {
            if ($scope.lightShow) {
                document.getElementById('preview_preview_main').innerHTML = document.getElementById('previewContent').innerHTML;
            } else {
                document.getElementById('preview_preview_main').innerHTML = $scope.previewContent;
            }
            $scope.previewPreviewShow = true;
            $scope.previewNotShow = false;
        };
        $scope.postPreviewOnClick = function() {
            if ($scope.lightShow) {
                document.getElementById('preview_post_main').innerHTML = document.getElementById('postContent').innerHTML;
            } else {
                document.getElementById('preview_post_main').innerHTML = $scope.postContent;
            }
            $scope.previewPostShow = true;
            $scope.previewNotShow = false;
        };
        $scope.exitPreviewOnClick = function() {
            $scope.previewNotShow = true;
            $scope.previewPreviewShow = false;
            $scope.previewPostShow = false;
        }

        $scope.submitPostOnClick = function() {
            var ArticleId;
            var Preview;
            var Content;
            var Category;
            if ($scope.lightShow) {
                ArticleId   = $scope.articleId;
                Preview     = document.getElementById('previewContent').innerHTML;
                Content     = document.getElementById('postContent').innerHTML
                Category    = $scope.articleCategory;

            } else {
                ArticleId   = $scope.articleId
                Preview     = $scope.previewContent
                Content     = $scope.postContent
                Category    = $scope.articleCategory;
            }
            console.debug(Category);
            var request = {
                params: {
                    'Action' : "CreateArticle",
                    'AccessKeyId' : 'plusplus7',
                    'SignatureMethod':"HmacSHA256",
                    'SignatureVersion':'1',
                    'Timestamp':'20160706',
                    "Version":"2016-06-12",
                    'ArticleId': ArticleId,
                    'Category': Category,
                    'Preview':Preview,
                    'Content':Content
                }
            }
            $http.post("http://" + window.location.host + "/api/CreateArticle", "", request).then(function successCallback(response){
                if (response["data"] == "") {
                    alert("Success!")
                } else {
                    alert("Failed!" + response)
                }
            }, function errorCallback(response) {
                alert("Failed!" + response)
            });
        }

        $scope.submitCategoryOnClick = function () {
            var request = {
                params: {
                    'Action' : "CreateCategory",
                    'AccessKeyId' : 'plusplus7',
                    'SignatureMethod':"HmacSHA256",
                    'SignatureVersion':'1',
                    'Timestamp':'20160706',
                    "Version":"2016-06-12",
                    'CategoryId': $scope.categoryId,
                    'CategoryDisplayName': $scope.categoryDisplayName,
                    'SectionId':$scope.categorySectionId,
                    'Type':$scope.categoryType
                }
            }
            $http.post("http://" + window.location.host + "/api/CreateCategory", "", request).then(function successCallback(response){
                if (response["data"] == "") {
                    alert("Success!")
                } else {
                    alert("Failed!" + response)
                }
            }, function errorCallback(response) {
                alert("Failed!" + response)
            });
        }
        for (var category in $scope.categories) {
            $scope.articleCategory = category;
            break;
        }
        $scope.articleSectorId = "blog";
        $scope.categoryOnChange = function(category) {
            if ($scope.articleCategory in $scope.categories) {
                $scope.articleSectorId = $scope.categories[$scope.articleCategory]["sector"];
            } else {
                $scope.articleSectorId = "blog";
            }
        };
        $scope.articleTitle = "";
        $scope.arthorLink = "http://plusplus7.com";
        $scope.arthorName = "plusplus7";
        $scope.timeTag = new Date().toLocaleDateString().replace("/", ".").replace("/", ".");

        $scope.previewContent = document.getElementById('previewContent').innerHTML;
        $scope.postContent = document.getElementById('postContent').innerHTML;
    });
